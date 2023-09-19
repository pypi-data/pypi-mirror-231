from __future__ import annotations

import traceback
from typing import Tuple

import numpy as np
import pandas as pd


from culib.utils.logs import get_local_logger
from culib.coils.basecoil import BaseCoil
from culib.field.df_field import calc_total_fields
from culib.field.calc_func import Bfield_axis_rectangular_solenoid
from culib.field.calc_func_3d import Bfield_3d_rectangular_solenoid
from culib.wires.data_wires import ROUND, SQUARE, FOIL
from culib.wires.basewire import Wire, DEFAULT_TEMP_DEGC


class RectangularCoil(BaseCoil):
    """
    Class definition of a Rectangular coil of wire, modeled as a finite solenoid of length "L_mm" of revolution axis "axis", of squared cross section with multiple layers of turns.

    Parameters
    ----------
    axis : str
        Name of the revolution axis of the coil. Must match with axis name in df_field (i.e: "x_mm", "y_mm" or "z_mm")
    X_in_mm : float
        Internal coil width in X in mm. Triggers recalculation of all parameters when setted if is_autorecalc is True.
    Y_in_mm : float
        Internal coil width in Y in mm. Triggers recalculation of all parameters when setted if is_autorecalc is True.
    T_mm : float
        Coil thickness, in mm
    L_mm : float
        Length of solenoid in the "axis". Triggers recalculation of all parameters when setted if is_autorecalc is True.
    wire : Wire
        Wire object to be used. Can be created via culib.Wire() (see doc/examples for wire declaration)

    name : str, optional
        Specifc Name/Label of the coil in case you want it different from the variable name, for information and loggings purposes. If not specified, will take name of the variable as coil name.
    pos_mm : float, optional
        Position of the middle of the coil on the revolution axis "axis". If not given at init, default is 0.0 mm.
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
        - 'default' : calc length via approximation by n * avg_rectangle_perimeter
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
    X_out_mm : float
        Coil outer width in X, accounting for coil thickness, in mm
    Y_out_mm : float
        Coil outer width in Y, accounting for coil thickness, in mm
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
    calc_X_out()
        Calculate X_out_m with thickness
    calc_Y_out()
        Calculate Y_out_mm with thickness
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
    >>> my_awg_wire = cul.RoundWire(d_in_mm = 0.511, t_insulation_mm=0.05)
    >>> my_hall3d_rectangular_coil = cul.RectangularCoil(
    ...     axis = 'z_mm',
    ...     X_in_mm = 45,
    ...     Y_in_mm = 57,
    ...     T_mm = 2.5,
    ...     L_mm = 78,
    ...     pos_mm = 0,
    ...     wire = my_awg_wire,
    ... )
    >>> my_hall3d_rectangular_coil.calc_n()
    508
    >>> my_hall3d_rectangular_coil.calc_res()
    8.905433925673478
    >>> my_hall3d_rectangular_coil.res_ohm
    8.905433925673478
    >>> my_hall3d_rectangular_coil.cur_A = 3
    >>> my_hall3d_rectangular_coil.calc_power()
    80.1489053310613

    ## Calculate field

    >>> my_hall3d_rectangular_coil.calc_field_at_center()
    19.53627468228739

    """

    def __init__(
        self,
        axis: str,
        X_in_mm: float,
        Y_in_mm: float,
        T_mm: float,
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
        # TODO (prio 2) : add corner radius for filleted corners
        **kwargs,
    ):
        if name is None:
            (filename, line_nr, func_name, text) = traceback.extract_stack()[-2]
            name = text[: text.find("=")].strip()
            if "(" in name:
                name = "dummy_coil"

        self.log = get_local_logger(f"{name}.RectangularCoil", **kwargs)
        self.name = name

        self._validate_X_in_mm(X_in_mm)
        self._validate_Y_in_mm(Y_in_mm)
        self._validate_thickness(T_mm)
        self._validate_length(L_mm)

        # Deduct geometrical attributes
        self.calc_X_out()  # will set self.X_out_mm
        self.calc_Y_out()  # will set self.Y_out_mm
        self.calc_X_avg()  # will set self.X_mm
        self.calc_Y_avg()  # will set self.Y_mm

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

        self.calc_volume()  # will set self.volume_mm3

    # Def specific attributes getters/setters (like for autorecalc of other params after resetting, ...)
    @property
    def X_out_mm(self):
        return self._X_out_mm

    @X_out_mm.setter
    def X_out_mm(self, value):
        err_msg = "cannot set X_out_mm directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    @property
    def X_in_mm(self):
        return self._X_in_mm

    @X_in_mm.setter
    def X_in_mm(self, value):
        self._validate_X_in_mm(value)
        if self._is_autorecalc:
            self.calc_X_out()
            self.calc_X_avg()
            self.trigger_all_coil_param_recalc_func()

    @property
    def X_mm(self):
        return self._X_mm

    @X_mm.setter
    def X_mm(self, value):
        err_msg = "cannot set X directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    @property
    def Y_out_mm(self):
        return self._Y_out_mm

    @Y_out_mm.setter
    def Y_out_mm(self, value):
        err_msg = "cannot set Y_out_mm directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    @property
    def Y_in_mm(self):
        return self._Y_in_mm

    @Y_in_mm.setter
    def Y_in_mm(self, value):
        self._validate_Y_in_mm(value)
        if self._is_autorecalc:
            self.calc_Y_out()
            self.calc_Y_avg()
            self.trigger_all_coil_param_recalc_func()

    @property
    def Y_mm(self):
        return self._Y_mm

    @Y_mm.setter
    def Y_mm(self, value):
        err_msg = "cannot set Y directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    @property
    def T_mm(self):
        return self._T_mm

    @T_mm.setter
    def T_mm(self, value):
        self._validate_thickness(value)
        if self._is_autorecalc:
            self.calc_X_out()
            self.calc_Y_out()
            self.calc_X_avg()
            self.calc_Y_avg()
            self.trigger_all_coil_param_recalc_func()

    @property
    def L_mm(self):
        return self._L_mm

    @L_mm.setter
    def L_mm(self, value):
        self._validate_length(value)
        if self._is_autorecalc:
            self.trigger_all_coil_param_recalc_func()

    ## Define input validation methods
    def _validate_X_in_mm(self, X_in_mm) -> None:
        """
        Check if dimension is correct type and >0.
        If OK, set validated values in self.X_in_mm.

        Parameters
        ----------
        X_in_mm

        Raises
        -------
        ValueError
            If param is not >0
        TypeError
            If param is not numeric
        """
        tuple_accepted_types = (int, np.int32, np.int64, float, np.float32, np.float64)
        if isinstance(X_in_mm, tuple_accepted_types):
            if X_in_mm > 0:
                self._X_in_mm = X_in_mm
            else:
                err_msg = f"cannot set negative X_in_mm. Got X_in_mm={X_in_mm}"
                self.log.error(err_msg)
                raise ValueError(err_msg)
        else:
            err_msg = f"X_in_mm specified is not numeric. Accepted types are {tuple_accepted_types}. Got X_in_mm={X_in_mm}"
            self.log.error(err_msg)
            raise TypeError(err_msg)

    def _validate_Y_in_mm(self, Y_in_mm) -> None:
        """
        Check if dimension is correct type and >0.
        If OK, set validated values in self.Y_in_mm.

        Parameters
        ----------
        Y_in_mm

        Raises
        -------
        ValueError
            If param is not >0
        TypeError
            If param is not numeric
        """
        tuple_accepted_types = (int, np.int32, np.int64, float, np.float32, np.float64)
        if isinstance(Y_in_mm, tuple_accepted_types):
            if Y_in_mm > 0:
                self._Y_in_mm = Y_in_mm
            else:
                err_msg = f"cannot set negative Y_in_mm. Got Y_in_mm={Y_in_mm}"
                self.log.error(err_msg)
                raise ValueError(err_msg)
        else:
            err_msg = f"Y_in_mm specified is not numeric. Accepted types are {tuple_accepted_types}. Got Y_in_mm={Y_in_mm}"
            self.log.error(err_msg)
            raise TypeError(err_msg)

    def _validate_thickness(self, T_mm) -> None:
        """
        Check if dimension is correct type and >0.
        If OK, set validated values in self.T_mm

        Parameters
        ----------
        T_mm

        Raises
        -------
        ValueError
            If param is not >0
        TypeError
            If param is not numeric
        """
        tuple_accepted_types = (int, np.int32, np.int64, float, np.float32, np.float64)
        if isinstance(T_mm, tuple_accepted_types):
            if T_mm > 0:
                self._T_mm = T_mm
            else:
                err_msg = f"cannot set negative T_mm. Got T_mm={T_mm}"
                self.log.error(err_msg)
                raise ValueError(err_msg)
        else:
            err_msg = f"T_mm specified is not numeric. Accepted types are {tuple_accepted_types}. Got T_mm={T_mm}"
            self.log.error(err_msg)
            raise TypeError(err_msg)

    def _validate_length(self, L_mm) -> None:
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
    def calc_X_out(self) -> float:
        self._X_out_mm = self.X_in_mm + 2 * self.T_mm
        return self._X_out_mm

    def calc_Y_out(self) -> float:
        self._Y_out_mm = self.Y_in_mm + 2 * self.T_mm
        return self._Y_out_mm

    def calc_X_avg(self) -> float:
        self._X_mm = round((self._X_out_mm + self._X_in_mm) / 2, 2)
        return self._X_mm

    def calc_Y_avg(self) -> float:
        self._Y_mm = round((self._Y_out_mm + self._Y_in_mm) / 2, 2)
        return self._Y_mm

    def calc_volume(self, **kwargs) -> float:
        """
        Calc available volume for wire inside solenoid coil.
        Store it in _vol_mm3 attribute and return it in mm^3
        For a full parallelepiped : Vol = X*Y*Z. So for a diff here : Vol = L*(X_out*Y_out - X_in*Y_in)
        """
        # log = get_local_logger(f"{self.name}.{'calc_volume'}", **kwargs)
        self.volume_mm3 = self.L_mm*(self.X_out_mm*self.Y_out_mm - self.X_in_mm*self.Y_in_mm)  # fmt: skip
        self.volume_eff_mm3 = None  # No calc of effective volume for the moment
        return self.volume_mm3

    # #TOCHECK
    def calc_n(self, **kwargs) -> int:
        log = get_local_logger(f"{self.name}.{'calc_n'}", **kwargs)
        # fmt: off
        # From defined  L, X_in, X_out, Y_in, Y_out, d_wire_out
        if self.wire.shape in (ROUND, SQUARE):
            self._n_layer = int(np.floor(self.T_mm / self.wire.d_out_mm))
            self._n_length = int(np.floor(self.L_mm / self.wire.d_out_mm))
        elif self.wire.shape == FOIL:
            self._n_layer = int(np.floor(self.T_mm / (self.wire.t_foil_mm + 2*self.wire.t_insulation_mm)))
            self._n_length = int(np.floor(self.L_mm / (self.wire.L_foil_mm + 2*self.wire.t_insulation_mm)))
        else:
            err_msg = f"unknown wire shape ({self.wire.shape}). Cannot calculate n."
            log.error(err_msg)
            raise NotImplementedError(err_msg)
        #fmt : on
        self._n = self._n_layer * self._n_length
        log.info(f"n_layer={self.n_layer}, n_length={self.n_length}, n={self.n}")
        return self.n

    # TOCHECK
    def calc_total_wire_length(self, **kwargs) -> float:
        log = get_local_logger(f"{self.name}.{'calc_total_wire_length'}", **kwargs)

        method = self.method_calc_total_wire_length
        # Default method is via approximation by n * avg rectangle perimeter
        if method == "default":
            self.lambda_wire_m = self.n * (2 * self.X_mm + 2 * self.Y_mm) / 1000
        # If method "via Volume"
        elif method == "volume":
            self.calc_volume()
            err_msg = "'volume' method not implemented yet for RectangularCoil"
            log.error(err_msg)
            raise NotImplementedError(err_msg)
            # if self.wire.shape in (ROUND, SQUARE):
            #     self.lambda_wire_m = (self.volume_eff_mm3 / self.wire.d_out_mm ** 2) / 1000
            # elif self.wire.shape==FOIL:
            #     self.lambda_wire_m = (self.volume_eff_mm3 / self.wire.L_foil_mm * self.wire.t_foil_mm) / 1000
            # else:
            #     err_msg = f"unknown wire shape ({self.wire.shape}). Cannot calculate lambda_wire_m."
            #     log.error(err_msg)
            #     raise ValueError(err_msg)
        else:
            err_msg = f"unknown method defined for wire length calculation ({method})"
            log.error(err_msg)
            raise ValueError(err_msg)
        return self.lambda_wire_m

    def calc_res(self, **kwargs) -> float:
        # log = get_local_logger(f"{self.name}.{'calc_res'}", **kwargs)
        self.calc_total_wire_length(method=self._method_calc_total_wire_length)
        self.res_ohm = self.lambda_wire_m * self.wire.eta_linres_ohmperm
        return self.res_ohm

    def calc_voltage(self, **kwargs) -> float:
        log = get_local_logger(f"{self.name}.{'calc_voltage'}", **kwargs)
        if self.cur_A is not None:
            self.vol_V = self.res_ohm * self.cur_A
        else:
            log.info("coil current cur_A not defined, cannot calculate voltage")
            self.vol_V = None
        return self.vol_V

    def calc_power(self, **kwargs) -> float:
        log = get_local_logger(f"{self.name}.{'calc_power'}", **kwargs)
        if self.cur_A is not None:
            self.pow_W = self.res_ohm * self.cur_A**2
        else:
            log.info("coil current cur_A not defined, cannot calculate power")
            self.pow_W = None
        return self.pow_W

    # TOCHECK : formula for inductance calculation
    def calc_inductance(self, **kwargs) -> float:
        """
        Calculate self-inductance thanks to Wheeler approximation.
        """
        log = get_local_logger(f"{self.name}.{'calc_inductance'}", **kwargs)
        if self.wire.shape in (ROUND, SQUARE):
            avg_width = 1e-3 * 0.5 * (self.X_mm + self.Y_mm)
            self.ind_mH = (1e-2 * avg_width**2 * self.n**2) / (3*avg_width + 9e-3*self.L_mm + 10e-3*self.T_mm)  # fmt: skip
        elif self.wire.shape == FOIL:
            err_msg = "inductance calc is not implemented yet for FOIL wire. Set ind_mH = None."
            log.warning(err_msg)
            self.ind_mH = None
        else:
            err_msg = f"unknown wire shape ({self.wire.shape}). Cannot calculate ind_mH"
            log.error(err_msg)
            raise ValueError(err_msg)
        return self.ind_mH

    def calc_time_constant(self, **kwargs) -> float:
        """
        Calculate time constant tau_ms defined as ratio self-inductance / resistance (in ms)
        """
        log = get_local_logger(f"{self.name}.{'calc_time_constant'}", **kwargs)
        try:
            self.tau_ms = self.ind_mH / self.res_ohm
        except TypeError:
            err_msg = f"missing parameter to calc tau_ms : self.ind_mH={self.ind_mH}, self.res_ohm={self.res_ohm}. Skipping calculation."
            log.warning(err_msg)
            self.tau_ms = None
        return self.tau_ms

    def calc_weight(self, **kwargs) -> float:
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
        calc_func=Bfield_axis_rectangular_solenoid,
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
        >>> my_wire = cul.RoundWire(d_in_mm = 0.511, t_insulation_mm=0.05)
        >>> mycoil = cul.RectangularCoil(
        ...     axis = 'z_mm',
        ...     X_in_mm = 45,
        ...     Y_in_mm = 57,
        ...     T_mm = 2.5,
        ...     L_mm = 78,
        ...     pos_mm = 12,
        ...     cur_A = 6.9,
        ...     wire = my_wire)
        >>> df_field = cul.init_df_field()

        # Use calc_field to update df_field (will write field in col "Bz_mycoil_mT")

        >>> df_field = mycoil.calc_field(df_field)

        # Write in a custom Series with ret_ser=True

        >>> df_field["Bz_mycustomname_mT"] = mycoil.calc_field(df_field, ret_ser=True)

        """
        log = get_local_logger(f"{self.name}.{'calc_field'}", **kwargs)

        try:
            field_ser = calc_func(
                df_field[self.axis] - self._get_pos_on_coil_axis(),
                X_coil_mm=self.X_mm,
                Y_coil_mm=self.Y_mm,
                L_coil_mm=self.L_mm,
                n_turn=self.n,
                I_coil_A=self.cur_A,
                **kwargs,
            )
        except TypeError:
            list_needed_param = ["_pos_mm", "_cur_A", "_X_mm", "_Y_mm", "_L_mm", "_n"]
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
            - "approximation" : from rough analytic : mu0 * n * cur_A / np.sqrt(L_mm**2 + ((X_mm+Y_mm)/2)**2)

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
                D_mm = (self.X_mm + self.Y_mm) / 2  # Approximate avg "diameter"
                B_mT = mu0 * self.n * self.cur_A / np.sqrt(self.L_mm**2 + D_mm**2)
            except TypeError:
                list_needed_param = ["_cur_A", "_X_mm", "_Y_mm", "_L_mm", "_n"]
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
        calc_func=Bfield_3d_rectangular_solenoid,
        ret_ser: bool = False,
        update_total: bool = True,
        is_delta_method: bool = False,
        delta_mm2: float = 1e-3,
        **kwargs,
    ) -> pd.DataFrame | (pd.Series, pd.Series, pd.Series):
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
        is_delta_method : bool, optional
            If True, will add a small constant in expressions in order to avoid potential divergence of ratios in arctan. Default is False.
            To be used in case of issue.
        delta_mm2 : float, optional
            Value of delta in mm2. Must be "sufficiently small to have a negligible effect on calculation". Default is 1e-3.

        Returns
        -------
        Updated DataFrame with 3 series or Tuple of 3 Series if ret_ser is True.

        Raises
        ------
        TypeError
            In case any parameter is missing for the field calculation

        Notes
        -----
        Finite Solenoid of Length L, single wire layer model (of mean X and Y)
        Integration of Biot-Savart law, as per https://doi.org/10.1063/5.0010982 (work from S. Hampton, R. A. Lane, R. M. Hedlof, R. E. Phillips and C. A. Ordonez)

        Examples
        --------
        >>> import culib as cul
        >>> my_wire = cul.RoundWire(d_in_mm = 0.511, t_insulation_mm=0.05)
        >>> mycoil = cul.RectangularCoil(
        ...     axis = 'z_mm',
        ...     X_in_mm = 45,
        ...     Y_in_mm = 57,
        ...     T_mm = 2.5,
        ...     L_mm = 78,
        ...     pos_mm = 12,
        ...     cur_A = 6.9,
        ...     wire = my_wire)
        >>> df_field = cul.init_df_field_3d(50,1)
        >>> df_field = mycoil.calc_field_3d(df_field)

        # In case of weird values, you can use is_delta_method to avoid divergence of ratios in arctan.
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
                X_coil_mm=self.X_mm,
                Y_coil_mm=self.Y_mm,
                L_coil_mm=self.L_mm,
                n_turn=self.n,
                I_coil_A=self.cur_A,
                is_delta_method=is_delta_method,
                delta_mm2=delta_mm2,
                **kwargs,
            )
        except TypeError:
            list_needed_param = [
                "_pos_x_mm",
                "_pos_y_mm",
                "_pos_z_mm",
                "_cur_A",
                "_X_mm",
                "_Y_mm",
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
