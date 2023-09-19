from __future__ import annotations

import traceback
from typing import Tuple

import numpy as np
import pandas as pd

from culib.utils.logs import get_local_logger
from culib.coils.basecoil import BaseCoil
from culib.field.df_field import calc_total_fields
from culib.field.calc_func import Bfield_axis_circular_solenoid
from culib.field.calc_func_3d import Bfield_3d_circular_solenoid
from culib.wires.data_wires import ROUND, SQUARE, FOIL
from culib.wires.basewire import Wire, DEFAULT_TEMP_DEGC


class CircularCoil(BaseCoil):
    """
    Class definition of a Circular coil of wire, modeled as a finite solenoid of length "L_mm" of revolution axis "axis", of squared cross section with multiple layers of turns.

    It allows integration of "real-life" characteristics, such as :

    - Coil thickness (because of an external radius and internal radius)
    - Number of turns calculation based on coil geometrical dimensions for a given wire size
    - Wire size declaration based on standard AWG sizes, or custom definition (i.e for squared section wire, ....)
    - Automatic recalculation of coils parameters in case of modification of geometric params or wire type (useful for wire selection and recalculation of all params based on suppliers capabilities)
    - Calculation of voltage and power needed based on current injected and resistance calculation

    Also integrates function for magnetic field calculation (only support magnetic field calculation along the coil revolution axis for the moment)

    Parameters
    ----------
    axis : str
        Name of the revolution axis of the coil. Must match with axis name in df_field (i.e: "x_mm", "y_mm" or "z_mm")
    r_out_mm : float
        External coil radius in mm. Triggers recalculation of all parameters when setted if is_autorecalc is True.
    r_in_mm : float
        Internal coil radius in mm. Triggers recalculation of all parameters when setted if is_autorecalc is True.
    L_mm : float
        Length of solenoid in the "axis". Triggers recalculation of all parameters when setted if is_autorecalc is True.
    wire : Wire
        Wire object to be used, to create via culib.Wire() (see doc/examples for wire declaration)
    name : str, optional
        Specifc Name/Label of the coil in case you want it different from the variable name, for information and loggings purposes. If not specified, will take name of the variable as coil name.
    pos_mm : float|Tuple[float, float, float], optional
        Position of the middle of the coil on the revolution axis "axis". Default is 0.0 mm. If specified as Tuple, indicate position in 3D as (x, y, z).
    n : int, optional
        Number of turn of wire in total (n_layer * n_length).
        If not given at init, it will be calculated automatically if awg_wire or wire dimensions are given.
        If none of these are given at init, just passes.
        Calculation model : assumes basic number of turns like squared stacked on top of each other (can change in future versions)
        Triggers recalculation of all parameters when setted if is_autorecalc is True.
    cur_A : float, optional
        Current in the wire in A. Triggers recalculation of all parameters when setted if is_autorecalc is True.
    temp_degC : float, optional
        Temperature of the coil in degC. Shared and passed to attached wire object to recalculate automatically resistance=f(temp).
    method_calc_total_wire_length : str, optional
        Define method for the calculation of total wire length, between :
        - 'default' : calc length via approximation by n * 2pi * r_avg
        - 'volume'  : calc length via volume_eff_mm3 / wire_section_area_mm2
        Note : 'default' method tends to slightly overestimate resistance by ~5-10% vs 'volume' method, which describes better a perfect coil.
        So 'default' is preferred as it adds a convenient error margin that we retrieve empirically with existing coils from suppliers poor winding capabilities said as "wild-winding" (i.e Hall3D coils). And even "orthocyclic-winding" a bit more optimized.
    is_autorecalc : bool, optional
        Enable or disable automatic coil parameters calculation. Default is True.
        If False, need to manually call calculation sequences for getting a coil parameter.
        (i.e for getting P_W after changing r_out_mm, the following sequence should be manually called :
        self.calc_r_avg_mm(), then self.calc_res(), then self.calc_voltage() and then self.calc_power())
    log_level : int|str, optional
        Level of loggings for this object (compatible type with logging standard lib, i.e:'WARNING', 10, ...)

    Attributes
    ----------
    Params
        All parameters given at init +
    T_mm : float
        Coil thickness, in mm
    volume_mm3 : float
        Inner volume of the coil, in mm^3
    volume_eff_mm3 : float
        Inner effective volume of the coil, useful for method_calc_total_wire_length='volume' only, in mm^3
    r_mm : float
        Average coil radius in mm (r_in_mm+r_out_mm)/2
    n_length : int
        Number of turn of wire in the length direction
    n_layer : int
        Number of layer of wire in the thickness direction
    lambda_wire_m : float
        Total length of wire wrapped, in m
    res_ohm : float
        Coil resistance at 20degC, in Ohm
    vol_V : float
        Coil voltage at 20degC, in V
    pow_W : float
        Coil power at 20degC, in W
    ind_mH : float
        Coil self-inductance estimation, in mH
    tau_ms : float
        Coil time constant, defined as L/R, in ms
    weight_g : float
        Coil weight deduced from totat wire length and wire material properties, in g

    Methods
    -------
    calc_r_avg_mm()
        Calculate r_mm
    calc_volume()
        Calculate volume_mm3 and effective volume (applicable for total_wire_length calculation method only)
    calc_n()
        Calculate n from geometric dimensions + wire dimensions
    calc_total_wire_length()
        Calculate total length of wire wrapped, with methodology written in method_calc_total_wire_length
    calc_res()
        Calculate coil resistance from length + lineic resistance at 20degC
    calc_voltage()
        Calculate coil voltage from current + resistance at 20degC
    calc_power()
        Calculate coil power from current + resistance at 20degC
    calc_field(df_field, calc_func)
        Returns field as Series from axis in df_field for calc_func specified

    Examples
    --------
    ## Declare coils with AWG

    >>> import culib as cul
    >>> my_awg_wire = cul.Wire(awg=22, t_insulation_mm=0.05, shape='round')
    >>> my_left_helmholtz_coil = cul.CircularCoil(
    ...     axis = 'x_mm',
    ...     r_out_mm = 50+5,
    ...     r_in_mm = 50-5,
    ...     L_mm = 15,
    ...     pos_mm = -50/2,
    ...     wire = my_awg_wire,
    ... )
    >>> my_left_helmholtz_coil.calc_n()
    260
    >>> my_left_helmholtz_coil.calc_res()
    4.212800432082095
    >>> my_left_helmholtz_coil.res_ohm
    4.212800432082095
    >>> my_left_helmholtz_coil.cur_A = 12
    >>> my_left_helmholtz_coil.calc_power()
    606.6432622198217

    ## Calculate field

    >>> df_field = cul.init_df_field(axis_length_mm = 160, res_step_mm=0.05)
    >>> df_field = my_left_helmholtz_coil.calc_field(df_field)
    >>> my_right_helmholtz_coil = cul.CircularCoil(
    ...    axis = 'x_mm',
    ...    r_out_mm = 50+5,
    ...    r_in_mm = 50-5,
    ...    L_mm = 15,
    ...    pos_mm = +50/2,
    ...    wire = my_awg_wire,
    ...    cur_A = 12,
    ... )
    >>> df_field = my_right_helmholtz_coil.calc_field(df_field)
    >>> homo_percent = cul.get_field_homo_at_pos(df_field, axis='x_mm', Baxis='Bx_total_mT', pos_mm=0.0, homo_region_mm=0.5)
    >>> round(homo_percent, 8)
    0.00050049

    ## Change wires of both coils to FOIL wire

    ### Check resistance value before change

    >>> my_left_helmholtz_coil.res_ohm
    4.212800432082095
    >>> my_foil_wire = cul.FoilWire(L_foil_mm = 5, t_foil_mm = 0.1)
    >>> my_left_helmholtz_coil.wire = my_foil_wire
    >>> my_right_helmholtz_coil.wire = my_foil_wire
    >>> my_left_helmholtz_coil.res_ohm
    1.0555751316061706

    ### Update df_field and calcs

    >>> df_field = my_left_helmholtz_coil.calc_field(df_field)
    >>> df_field = my_right_helmholtz_coil.calc_field(df_field)
    >>> df_field = cul.calc_total_fields(df_field)

    ### Check wire type doesn't change anything on field topology

    >>> homo_percent = cul.get_field_homo_at_pos(df_field, axis='x_mm', Baxis='Bx_total_mT', pos_mm=0.0, homo_region_mm=0.5)
    >>> round(homo_percent, 8)
    0.00050049

    """

    def __init__(
        self,
        axis: str,
        r_in_mm: float,
        r_out_mm: float,
        L_mm: float,
        wire: Wire,
        name: str = None,
        pos_mm: float | Tuple[float, float, float] = 0.0,
        n: int = None,
        cur_A: float = None,
        temp_degC: float = DEFAULT_TEMP_DEGC,
        method_calc_total_wire_length: str = "default",
        is_autorecalc: bool = True,
        log_level: int | str = None,
        **kwargs,
    ):
        if name is None:
            (filename, line_nr, func_name, text) = traceback.extract_stack()[-2]
            name = text[: text.find("=")].strip()
            if "(" in name:
                name = "dummy_coil"

        self.log = get_local_logger(
            f"{name}.CircularCoil", log_level=log_level, **kwargs
        )
        self.name = name

        self._validate_radiuses(r_in_mm, r_out_mm)
        self._validate_length(L_mm)

        # Deduct geometrical attributes
        self.calc_r_avg_mm()  # will set self.r_mm
        self.calc_thickness()  # will set self.T_mm

        super().__init__(
            name=name,
            axis=axis,
            wire=wire,
            pos_mm=pos_mm,
            n=n,
            cur_A=cur_A,
            temp_degC=temp_degC,
            method_calc_total_wire_length=method_calc_total_wire_length,
            is_autorecalc=is_autorecalc,
            logger=self.log,
            log_level=log_level,
            **kwargs,
        )

        # If not set
        self.calc_volume()  # will set self.volume_mm3

    # Def specific attributes getters/setters (like for autorecalc of other params after resetting, ...)
    @property
    def r_out_mm(self):
        return self._r_out_mm

    @r_out_mm.setter
    def r_out_mm(self, value):
        self._validate_radiuses(self._r_in_mm, value)
        if self._is_autorecalc:
            self.calc_r_avg_mm()
            self.calc_thickness()
            self.trigger_all_coil_param_recalc_func()

    @property
    def r_in_mm(self):
        return self._r_in_mm

    @r_in_mm.setter
    def r_in_mm(self, value):
        self._validate_radiuses(value, self._r_out_mm)
        if self._is_autorecalc:
            self.calc_r_avg_mm()
            self.calc_thickness()
            self.trigger_all_coil_param_recalc_func()

    @property
    def r_mm(self):
        return self._r_mm

    @r_mm.setter
    def r_mm(self, value):
        err_msg = "cannot set r directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    @property
    def L_mm(self):
        return self._L_mm

    @L_mm.setter
    def L_mm(self, value):
        self._validate_length(value)
        if self._is_autorecalc:
            self.trigger_all_coil_param_recalc_func()

    @property
    def T_mm(self):
        return self._T_mm

    @T_mm.setter
    def T_mm(self, value):
        err_msg = "cannot set T directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    ## Define input validation methods
    def _validate_radiuses(self, r_in_mm, r_out_mm) -> None:
        """
        Check if radiuses are correct type, >0 and r_in_mm <= r_out_mm.
        If OK, set validated values in self.r_in_mm and self.r_out_mm.

        Parameters
        ----------
        r_in_mm
            Inner radius in mm
        r_out_mm
            Outer radius in mm

        Raises
        -------
        ValueError
            If radiuses are negative or if r_in_mm > r_out_mm
        TypeError
            If radiuses are not numeric
        """
        tuple_accepted_types = (int, np.int32, np.int64, float, np.float32, np.float64)
        if isinstance(r_in_mm, tuple_accepted_types) and isinstance(r_out_mm, tuple_accepted_types):  # fmt: skip
            if (r_in_mm > 0) and (r_out_mm > 0):
                if r_in_mm < r_out_mm:
                    self._r_in_mm = r_in_mm
                    self._r_out_mm = r_out_mm
                else:
                    err_msg = f"outer radius is not greater than inner radius. Got r_in_mm={r_in_mm} and r_out_mm={r_out_mm}"
                    self.log.error(err_msg)
                    raise ValueError(err_msg)
            else:
                err_msg = f"cannot set negative radius. Got r_in_mm={r_in_mm} and r_out_mm={r_out_mm}"
                self.log.error(err_msg)
                raise ValueError(err_msg)
        else:
            err_msg = f"radiuses specified are not numeric. Accepted types are {tuple_accepted_types}. Got r_in_mm={r_in_mm} and r_out_mm={r_out_mm}"
            self.log.error(err_msg)
            raise TypeError(err_msg)

    def _validate_length(self, L_mm):
        """
        Check if coil length is correct type and >0 .
        If OK, set validated value in self.L_mm.

        Parameters
        ----------
        L_mm
            Coil length in mm

        Raises
        -------
        ValueError
            If length is not >0
        TypeError
            If length is not numeric
        """
        tuple_accepted_types = (int, np.int32, np.int64, float, np.float32, np.float64)
        if isinstance(L_mm, tuple_accepted_types):
            if L_mm > 0:
                self._L_mm = L_mm
            else:
                err_msg = f"cannot set negative length. Got L_mm={L_mm}"
                self.log.error(err_msg)
                raise ValueError(err_msg)
        else:
            err_msg = f"length specified is not numeric. Accepted types are {tuple_accepted_types}. Got L_mm={L_mm}"
            self.log.error(err_msg)
            raise TypeError(err_msg)

    ## Define calc methods
    def calc_r_avg_mm(self):
        self._r_mm = round((self._r_out_mm + self._r_in_mm) / 2, 2)
        return self._r_mm

    def calc_thickness(self):
        self._T_mm = round((self._r_out_mm - self._r_in_mm), 2)
        return self._T_mm

    def calc_volume(self, **kwargs):
        """
        Calc available volume for wire inside solenoid coil.
        Store it in _vol_mm3 attribute and return it in mm^3
        For a full cylinder : Vol = pi*R^2*h. So for a diff here : Vol = pi*(R_out^2 - R_in^2)*L
        """
        log = get_local_logger(f"{self.name}.{'calc_volume'}", **kwargs)
        # fmt: off
        self.volume_mm3 = np.pi * (self.r_out_mm**2 - self.r_in_mm**2) * self.L_mm
        # Calc effective volume accounting for losses due to wire turn count
        if self.wire.shape in (ROUND, SQUARE):
            volume_eff_outer_mm3 = np.pi/4*(self.L_mm - self.wire.d_out_mm)*(2*self.r_in_mm + 2*self.wire.d_out_mm*np.floor(self.T_mm/self.wire.d_out_mm))**2 #fmt: skip
            volume_eff_inner_mm3 = np.pi/4*(self.L_mm - self.wire.d_out_mm)*(2*self.r_in_mm)**2
        elif self.wire.shape == FOIL:
            #TOCHECK (prio 2) : effective volume for foil wire
            t_foil_out_mm = self.wire.t_foil_mm + 2*self.wire.t_insulation_mm
            L_foil_out_mm = self.wire.L_foil_mm + 2*self.wire.t_insulation_mm
            volume_eff_outer_mm3 = np.pi/4*(self.L_mm - L_foil_out_mm)*(2*self.r_in_mm + 2*t_foil_out_mm*np.floor(self.T_mm/t_foil_out_mm))**2
            volume_eff_inner_mm3 = np.pi/4*(self.L_mm - L_foil_out_mm)*(2*self.r_in_mm)**2
        else:
            err_msg = f"unknown wire shape ({self.wire.shape}). Cannot calculate volume_eff_mm3."
            log.error(err_msg)
            raise NotImplementedError(err_msg)
        # fmt: on
        self.volume_eff_mm3 = volume_eff_outer_mm3 - volume_eff_inner_mm3
        return self.volume_mm3

    def calc_n(self, **kwargs):
        log = get_local_logger(f"{self.name}.{'calc_n'}", **kwargs)
        # fmt: off
        # From defined L, r_in, r_out, d_wire_out
        if self.wire.shape in (ROUND, SQUARE):
            self._n_layer = int(np.floor((self.r_out_mm - self.r_in_mm) / self.wire.d_out_mm))
            self._n_length = int(np.floor(self.L_mm / self.wire.d_out_mm))
        elif self.wire.shape == FOIL:
            self._n_layer = int(np.floor((self.r_out_mm - self.r_in_mm) / (self.wire.t_foil_mm + 2*self.wire.t_insulation_mm)))
            self._n_length = int(np.floor(self.L_mm / (self.wire.L_foil_mm + 2*self.wire.t_insulation_mm)))
        else:
            err_msg = f"unknown wire shape ({self.wire.shape}). Cannot calculate n."
            log.error(err_msg)
            raise NotImplementedError(err_msg)
        # fmt: on
        self._n = self._n_layer * self._n_length
        log.info(f"n_layer={self.n_layer}, n_length={self.n_length}, n={self.n}")
        return self.n

    def calc_total_wire_length(self, **kwargs):
        log = get_local_logger(f"{self.name}.{'calc_total_wire_length'}", **kwargs)
        # fmt: off
        method = self.method_calc_total_wire_length
        # Default method is via approximation by n * 2pi * r_avg
        if(method == 'default'):
            self.lambda_wire_m = 2*np.pi * self.n * self.r_mm / 1000
        # If method "via Volume"
        elif(method == 'volume'):
            self.calc_volume()
            if self.wire.shape in (ROUND, SQUARE):
                self.lambda_wire_m = (self.volume_eff_mm3 / self.wire.d_out_mm ** 2) / 1000
            elif self.wire.shape==FOIL:
                self.lambda_wire_m = (self.volume_eff_mm3 / self.wire.L_foil_mm*self.wire.t_foil_mm) / 1000
            else:
                err_msg = f"unknown wire shape ({self.wire.shape}). Cannot calculate lambda_wire_m."
                log.error(err_msg)
                raise ValueError(err_msg)
        # fmt: on
        else:
            err_msg = f"unknown method defined for wire length calculation ({method})"
            log.error(err_msg)
            raise ValueError(err_msg)
        return self.lambda_wire_m

    def calc_res(self, **kwargs):
        # log = get_local_logger(f"{self.name}.{'calc_res'}", **kwargs)
        self.calc_total_wire_length(method=self._method_calc_total_wire_length)
        self.res_ohm = self.lambda_wire_m * self.wire.eta_linres_ohmperm
        return self.res_ohm

    def calc_voltage(self, **kwargs):
        log = get_local_logger(f"{self.name}.{'calc_voltage'}", **kwargs)
        if self.cur_A is not None:
            self.vol_V = self.res_ohm * self.cur_A
        else:
            log.info("coil current cur_A not defined, cannot calculate voltage")
            self.vol_V = None
        return self.vol_V

    def calc_power(self, **kwargs):
        log = get_local_logger(f"{self.name}.{'calc_power'}", **kwargs)
        if self.cur_A is not None:
            self.pow_W = self.res_ohm * self.cur_A**2
        else:
            log.info("Coil current cur_A not defined, cannot calculate power")
            self.pow_W = None
        return self.pow_W

    # TOCHECK : formula for inductance calculation
    def calc_inductance(self, **kwargs):
        """
        Calculate self-inductance thanks to Wheeler approximation.
        """
        log = get_local_logger(f"{self.name}.{'calc_inductance'}", **kwargs)
        if self.wire.shape in (ROUND, SQUARE):
            self.ind_mH = (7.9e-3 * 4e-6*self.r_mm**2 * self.n**2) / (3*2e-3*self.r_mm + 9e-3*self.L_mm + 10e-3*self.T_mm)  # fmt: skip
        elif self.wire.shape == FOIL:
            err_msg = "inductance calc is not implemented yet for FOIL wire. Set ind_mH = None."
            log.warning(err_msg)
            self.ind_mH = None
        else:
            err_msg = f"unknown wire shape ({self.wire.shape}). Cannot calculate ind_mH"
            log.error(err_msg)
            raise NotImplementedError(err_msg)

        return self.ind_mH

    def calc_time_constant(self, **kwargs):
        """
        Calculate time constant tau_ms defined as ratio self-inductance / resistance (in ms)
        """
        log = get_local_logger(f"{self.name}.{'calc_time_constant'}", **kwargs)
        try:
            self.tau_ms = self.ind_mH / self.res_ohm
        except TypeError:
            err_msg = f"missing parameter to calc tau_ms : self.ind_mH={self.ind_mH}, self.res_ohm={self.res_ohm}. Skipping calculation."  # fmt: skip
            log.warning(err_msg)
            self.tau_ms = None
        return self.tau_ms

    def calc_weight(self, **kwargs):
        """
        Calculate coil's weight based on length of wire and lineic mass density of the wire
        Assumed to be constant over temperature for simplicity
        """
        # log = get_local_logger(f"{self.name}.{'calc_weight'}", **kwargs)
        self._weight_g = self.lambda_wire_m * self.wire.mass_lindensity_gperm
        return self._weight_g

    def calc_field(
        self,
        df_field,
        calc_func=Bfield_axis_circular_solenoid,
        ret_ser: bool = False,
        update_total: bool = True,
        **kwargs,
    ) -> pd.DataFrame | pd.Series:
        """
        Calculate Bfield along spatial axis 'axis' contained in df_field
        (i.e if axis of the coil is 'x_mm', it will calc Bx=f(x)).
        Returns an updated df_field with calculated field in column "B*axis*_*coilname*_mT".

        If ret_ser is True : will return field as a Series only.

        Parameters
        ----------
        df_field : pd.DataFrame
            Dataframe containing 'axis' column matching self.axis (i.e "x_mm")
        calc_func : function, optional
            Name of the calculation function f returning Baxis=f(axis).
            Only support 1D for the moment. Default is Bfield_axis_rectangular_solenoid
        ret_ser : bool, optional
            If True, function will return a pd.Series only (not an updated df). Default is False.
        update_total : bool, optional
            If True, will apply calc_total_fields() to df_field before returning df_field. No effect if ret_ser is True. Default is True.

        Returns
        -------
        Updated DataFrame df_Field by default. Or a pd.Series if ret_ser is True.

        Raises
        ------
        TypeError
            In case any parameter is missing for the field calculation

        Examples
        --------
        >>> import culib as cul
        >>> mycoil = CircularCoil(
        ...     axis = 'x_mm',
        ...     r_out_mm = 50+5,
        ...     r_in_mm = 50-5,
        ...     L_mm = 15,
        ...     pos_mm = -50/2,
        ...     wire = cul.Wire(awg=22, shape='round'),
        ...     cur_A = 12)
        >>> df_field = cul.init_df_field(axis_length_mm=160, res_step_mm=0.05)
        >>> df_field["Bx_mycoil_mT"] = mycoil.calc_field(df_field, ret_ser=True)
        """
        log = get_local_logger(f"{self.name}.{'calc_field'}", **kwargs)
        try:
            field_ser = calc_func(
                df_field[self.axis] - self._get_pos_on_coil_axis(),
                r_coil_mm=self.r_mm,
                L_coil_mm=self.L_mm,
                n_turn=self.n,
                I_coil_A=self.cur_A,
                **kwargs,
            )
        except TypeError:
            list_needed_param = ["_pos_mm", "_cur_A", "_r_mm", "_L_mm", "_n"]
            list_missing_param = [p[1:] for p in list_needed_param if self.__dict__[p] is None]  # fmt: skip
            err_msg = f"missing needed coils parameters for field calculation : {list_missing_param}"  # fmt: skip
            log.error(err_msg)
            raise TypeError(err_msg)

        if ret_ser:
            return field_ser
        else:
            # Write field value in df_field
            field_col_name = f"B{self.axis[0]}_{self.name}_mT"
            df_field[field_col_name] = field_ser
            if update_total:
                df_field = calc_total_fields(df_field)
            return df_field

    def calc_field_at_center(self, method: str = "default", **kwargs) -> float:
        """
        Get field value of coil axis component at coil center. Simplified call from calc_field()

        Parameters
        ----------
        method : str, optional
            - "default" will calculate from calc_field() method and get from center (with full computation)
            - "approximation" : from rough analytic : mu0 * n * cur_A / np.sqrt(L_mm**2 + D_mm**2)

        Returns
        -------
        B_mT : float
            Field value at center of main component (Bx if coil axis is x, Bz if z...) in mT
        """
        log = get_local_logger(f"{self.name}.{'calc_field_at_center'}", **kwargs)

        if method == "default":
            dummy_df_field = {self.axis: self._get_pos_on_coil_axis()}
            B_mT = self.calc_field(dummy_df_field, ret_ser=True)
        elif method == "approximation":
            mu0 = 4 * np.pi * 1e-1  # in mT.mm/A
            try:
                D_mm = 2 * self.r_mm
                B_mT = mu0 * self.n * self.cur_A / np.sqrt(self.L_mm**2 + D_mm**2)
            except TypeError:
                list_needed_param = ["_cur_A", "_r_mm", "_L_mm", "_n"]
                list_missing_param = [
                    p[1:] for p in list_needed_param if self.__dict__[p] is None
                ]
                err_msg = f"missing needed coils parameters for field calculation : {list_missing_param}"
                log.error(err_msg)
                raise TypeError(err_msg)
            except Exception as e:
                err_msg = "unknown error during field calculation"
                log.error(err_msg)
                raise type(e)(err_msg)
        else:
            err_msg = f"unknown method for calculating field (method={method})"
            log.error(err_msg)
            raise ValueError(err_msg)

        return B_mT

    def calc_field_3d(
        self,
        df_field: pd.DataFrame,
        calc_func=Bfield_3d_circular_solenoid,
        ret_ser: bool = False,
        update_total: bool = True,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Calculate all 3 field components Bx=f(x,y,z), By=f(x,y,z) and Bz=f(x,y,z).
        Take Position (x,y,z) from df_field.
        Returns a df with the 3 calculated components in columns "Bx_*coilname*_mT", "By_*coilname*_mT" and "Bz_*coilname*_mT".
        If ret_ser is True : will return fields as a tuple of 3 Series only.

        Parameters
        ----------
        df_field : pd.DataFrame
            Dataframe containing 'axis' columns "x_mm", "y_mm" and "z_mm"
        calc_func : function, optional
            Name of the 3d calculation function. Default is Bfield_3d_rectangular_solenoid
        ret_ser : bool, optional
            If True, function will return a pd.Series only (not an updated df). Default is False.
        update_total : bool, optional
            If True, will apply calc_total_fields() to df_field before returning df_field. No effect if ret_ser is True. Default is True.

        Returns
        -------
        Updated DataFrame with 3 series or Tuple of 3 Series if ret_ser is True.

        Raises
        ------
        TypeError
            In case any parameter is missing for the field calculation

        Notes
        -----
        Finite Solenoid of Length L, single wire layer model (of mean radius
        Integration of Biot-Savart law, as per https://doi.org/10.1063/5.0010982 (work from S. Hampton, R. A. Lane, R. M. Hedlof, R. E. Phillips and C. A. Ordonez)

        Examples
        --------
        >>> import culib as cul
        >>> my_wire = cul.RoundWire(d_in_mm = 0.511, t_insulation_mm=0.05)
        >>> mycoil = cul.CircularCoil(
        ...     axis = 'x_mm',
        ...     r_in_mm = 45,
        ...     r_out_mm = 57,
        ...     L_mm = 30,
        ...     pos_mm = 12,
        ...     cur_A = 6.9,
        ...     wire = my_wire)
        >>> df_field = cul.init_df_field_3d()
        >>> df_field = mycoil.calc_field_3d(df_field)
        """
        log = get_local_logger(f"{self.name}.{'calc_field'}", **kwargs)

        try:
            ser_Bx, ser_By, ser_Bz = calc_func(
                df_field,
                coil_axis=self.axis,
                pos_x_mm=self.pos_x_mm,
                pos_y_mm=self.pos_y_mm,
                pos_z_mm=self.pos_z_mm,
                r_coil_mm=self.r_mm,
                L_coil_mm=self.L_mm,
                n_turn=self.n,
                I_coil_A=self.cur_A,
                **kwargs,
            )
        except TypeError:
            list_needed_param = [
                "_pos_x_mm",
                "_pos_y_mm",
                "_pos_z_mm",
                "_cur_A",
                "_r_mm",
                "_L_mm",
                "_n",
            ]
            list_missing_param = [p[1:] for p in list_needed_param if self.__dict__[p] is None]  # fmt: skip
            err_msg = f"missing needed coils parameters for field calculation : {list_missing_param}"  # fmt: skip
            log.error(err_msg)
            raise TypeError(err_msg)

        if ret_ser:
            return ser_Bx, ser_By, ser_Bz
        else:
            # Write field values into df_field
            df_field[f"Bx_{self.name}_mT"] = ser_Bx
            df_field[f"By_{self.name}_mT"] = ser_By
            df_field[f"Bz_{self.name}_mT"] = ser_Bz
            if update_total:
                df_field = calc_total_fields(df_field)
            return df_field
