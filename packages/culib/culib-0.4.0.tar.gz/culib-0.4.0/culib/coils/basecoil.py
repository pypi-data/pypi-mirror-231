from __future__ import annotations

import logging
import traceback
from decimal import Decimal

import numpy as np

from culib.utils.logs import get_local_logger
from culib.wires.basewire import Wire, DEFAULT_TEMP_DEGC
from culib.field.getters import is_valid_pos_1d, is_valid_pos_3d
from culib.field.validate import is_valid_axis


class BaseCoil:
    """
    Generic parent class to be overriden by specific coils. Using it as-is doesn't bring anything.
    """

    def __init__(
        self,
        axis: str,
        wire: Wire,
        name: str = None,
        pos_mm: float | tuple[float, float, float] = 0.0,
        n: int = None,
        cur_A: float = None,
        temp_degC: float = DEFAULT_TEMP_DEGC,
        method_calc_total_wire_length: str = "default",
        is_autorecalc: bool = True,
        logger: logging.Logger = None,
        log_level: int | str = None,
        **kwargs,
    ):
        # Define attributes that will be overriden by subclasses
        self._n_length = None
        self._n_layer = None
        self._weight_g = None

        # Set attributes given
        # TODO (prio 2) : add default wire in case wire is undefined (just for field plot purposes ?)
        self._validate_wire(wire)
        self._wire.trigger_all_coil_param_recalc_func = self.trigger_all_coil_param_recalc_func  # fmt: skip
        self._wire.trigger_elec_coil_param_recalc_func = self.trigger_elec_coil_param_recalc_func  # fmt: skip
        if logger:
            self.log = logger
            self._wire.log = logger
        else:
            if name is None:
                filename, line_nr, func_name, text = traceback.extract_stack()[-2]  # fmt: skip
                name = text[: text.find("=")].strip()
                if "(" in name:
                    name = "dummy_coil"
            self.log = get_local_logger(f"{name}.BaseCoil", log_level=log_level, **kwargs)  # fmt: skip
            self._wire.log = self.log

        self._log_level = log_level if log_level is not None else self.log.getEffectiveLevel()  # fmt: skip

        self.name = name
        self._validate_axis(axis)
        self._is_autorecalc = is_autorecalc
        self._wire._is_autorecalc = is_autorecalc
        self._cur_A = cur_A
        self._method_calc_total_wire_length = method_calc_total_wire_length
        self._temp_degC = temp_degC
        self._validate_pos_mm(pos_mm)
        if n is not None:
            self._validate_n(n)
        else:
            self.log.info("n not specified, will calculate it from geometry and wire specs")  # fmt: skip
            self._n = self.calc_n()

        # Calculate last attributes from all inputs
        self._wire.temp_degC = temp_degC  # Will call trigger_elec_coil_param_recalc_func() and set self.lambda_wire_mm, self.res_ohm, self.vol_V, self.pow_W, self.weight_g, self.ind_mH

    # Def specific attributes getters/setters (like for autorecalc of other params after resetting, ...)
    @property
    def is_autorecalc(self):
        return self._is_autorecalc

    @is_autorecalc.setter
    def is_autorecalc(self, value):
        self._is_autorecalc = value
        if self._is_autorecalc:
            self.trigger_all_coil_param_recalc_func()

    @property
    def log_level(self):
        return self._log_level

    @log_level.setter
    def log_level(self, value):
        self._log_level = value
        self.log.setLevel(value)

    @property
    def axis(self):
        return self._axis

    @axis.setter
    def axis(self, value):
        self._validate_axis(value)

    @property
    def pos_mm(self):
        return self._pos_mm

    @pos_mm.setter
    def pos_mm(self, value):
        self._validate_pos_mm(value)

    @property
    def pos_x_mm(self):
        return self._pos_x_mm

    @pos_x_mm.setter
    def pos_x_mm(self, value):
        self._validate_single_pos_mm(value, "x_mm")

    @property
    def pos_y_mm(self):
        return self._pos_y_mm

    @pos_y_mm.setter
    def pos_y_mm(self, value):
        self._validate_single_pos_mm(value, "y_mm")

    @property
    def pos_z_mm(self):
        return self._pos_z_mm

    @pos_z_mm.setter
    def pos_z_mm(self, value):
        self._validate_single_pos_mm(value, "z_mm")

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._validate_n(value)
        if self._is_autorecalc:
            # TODO (prio 2) : add validation recalc, put warning if not OK
            self.trigger_elec_coil_param_recalc_func()

    @property
    def n_layer(self):
        return self._n_layer

    @n_layer.setter
    def n_layer(self, value):
        err_msg = "cannot set n_layer directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    @property
    def n_length(self):
        return self._n_length

    @n_length.setter
    def n_length(self, value):
        err_msg = "cannot set n_length directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    @property
    def cur_A(self):
        return self._cur_A

    @cur_A.setter
    def cur_A(self, value):
        self._cur_A = value
        if self._is_autorecalc:
            self.calc_voltage()
            self.calc_power()

    @property
    def wire(self):
        return self._wire

    @wire.setter
    def wire(self, value):
        self.log.info(f"modifying full wire of {self.name} coil")
        self._validate_wire(value)
        if self._is_autorecalc:
            self.log.info("recalculating coils parameters from new wire")
            self.trigger_all_coil_param_recalc_func()

    @property
    def method_calc_total_wire_length(self):
        return self._method_calc_total_wire_length

    @method_calc_total_wire_length.setter
    def method_calc_total_wire_length(self, value):
        self._method_calc_total_wire_length = value
        if self._is_autorecalc:
            self.trigger_elec_coil_param_recalc_func()

    @property
    def temp_degC(self):
        return self._temp_degC

    @temp_degC.setter
    def temp_degC(self, value):
        self._temp_degC = value
        self.wire.temp_degC = value  # Will retrigger the full calc

    @property
    def weight_g(self):
        return self._weight_g

    @weight_g.setter
    def weight_g(self, value):
        err_msg = "cannot set weight directly"
        self.log.debug(err_msg)
        raise AttributeError(err_msg)

    # METHODS
    ## Define generic methods
    def __repr__(self):
        """
        Represent the coil as a dictionary of all its parameters
        """
        ret_dict = self.__dict__.copy()

        # Remove param to not show at all
        ret_dict.pop("_log_level")

        # Manage coil dict without wire
        ## Remove wire from dict for the moment
        ret_dict.pop("_wire")
        ## Remove the '_' prefix at the beginning of "private" params for readability
        list_keys_to_correct = [key for key in ret_dict if key.startswith("_")]
        for key in list_keys_to_correct:
            ret_dict[key[1:]] = ret_dict[key]
            ret_dict.pop(key)
        # Round floats for readability (up to 3 digits after comma, otherwise display as scientific notation)
        for key in ret_dict.keys():
            if isinstance(ret_dict[key], (float, np.float64)):
                rounded_value = round(ret_dict[key], 3)
                if rounded_value != 0.0 or "pos" in key:
                    ret_dict[key] = rounded_value
                else:
                    ret_dict[key] = f"{Decimal(ret_dict[key]):.3e}"
            elif key == "pos_mm" and isinstance(ret_dict[key], tuple):
                str_pos_mm_to_display = "("
                for pos in ret_dict[key]:
                    str_pos_mm_to_display += f"{round(pos, 3)}，"  # Not a regular comma (fullwidth comma U+FF0C)
                ret_dict[key] = str_pos_mm_to_display[:-1] + ")"

        ## Sort alphabetically and return dict as str
        ret_dict = dict(sorted(ret_dict.items()))
        str_ret_dict_coil = str(ret_dict).replace(',', ',\n').replace('}',',\n') + " 'wire': {\n"  # fmt: skip

        # Manage wire dict
        str_ret_dict_wire = self._wire.__repr__()
        str_ret_dict_wire = str_ret_dict_wire.replace('{','    ').replace(',\n ' , ',\n    ') + '}'  # fmt: skip

        # Concat str(ret_dict)
        return str_ret_dict_coil + str_ret_dict_wire

    ## Define input validation methods
    def _validate_wire(self, wire) -> None:
        """
        Check if wire argument has correct type and set it in self.wire if OK

        Raises
        -------
        TypeError
            If wire is not a culib Wire object
        """
        if isinstance(wire, Wire):
            self._wire = wire
        else:
            err_msg = f"wire specified is not a culib Wire object. Got wire = {wire} of type : {type(wire)}"  # fmt: skip
            try:
                self.log.error(err_msg)
            finally:
                raise TypeError(err_msg)

    def _validate_n(self, n) -> None:
        """
        Check if n is correct type and >0. If OK, set validated value in self.n.

        Parameters
        ----------
        n
            Number of turns

        Raises
        -------
        ValueError
            If n is not >0
        TypeError
            If n is not numeric
        """
        accepted_types = (int, np.int32, np.int64)
        if isinstance(n, accepted_types):
            if n > 0:
                self._n = n
            else:
                err_msg = f"cannot set negative or null number of turns. Got n={n}"
                self.log.error(err_msg)
                raise ValueError(err_msg)
        else:
            err_msg = f"n specified is not an integer. Accepted types are {accepted_types}. Got n={n}"  # fmt: skip
            self.log.error(err_msg)
            raise TypeError(err_msg)

    def _validate_axis(self, axis) -> None:
        """
        Check if axis is correct type and matching 'x_mm', 'y_mm' or 'z_mm'. If OK, set validated value in self.axis.

        Parameters
        ----------
        axis

        Raises
        -------
        ValueError
            If axis is not in ('x_mm', 'y_mm', 'z_mm')
        TypeError
            If axis is not a string
        """
        if is_valid_axis(axis, enable_raise=True, log=self.log):
            self._axis = axis

    def _validate_pos_mm(self, pos_mm) -> None:
        """
        Check if pos_mm is correct and handle if single value or Tuple[float, float, float]

        Parameters
        ----------
        pos_mm

        """
        if is_valid_pos_1d(pos_mm, enable_raise=False, log=self.log):
            self._pos_mm = pos_mm
            for axis in ("x_mm", "y_mm", "z_mm"):
                pos_mm_value = pos_mm if axis == self.axis else 0.0
                setattr(self, f"_pos_{axis}", pos_mm_value)
        elif is_valid_pos_3d(pos_mm, enable_raise=True, log=self.log):
            self._pos_mm = pos_mm
            self._pos_x_mm = pos_mm[0]
            self._pos_y_mm = pos_mm[1]
            self._pos_z_mm = pos_mm[2]
        else:
            err_msg = f"pos_mm is either numeric nor a tuple of 3 numeric. Got pos_mm={pos_mm}"
            self.log.error(err_msg)
            raise TypeError(err_msg)

    def _validate_single_pos_mm(self, pos_mm, single_axis: str) -> None:
        if is_valid_pos_1d:
            setattr(self, f"_pos_{single_axis}", pos_mm)
        else:
            err_msg = f"pos_{single_axis} is not numeric. Got {pos_mm}"
            self.log.error(err_msg)
            raise TypeError(err_msg)

    ## Define general methods
    def _get_pos_on_coil_axis(self) -> float:
        return getattr(self, f"_pos_{self.axis}")

    ## Define methods to override Wire method for recalculating coil params after modif of self.wire attributes
    def trigger_elec_coil_param_recalc_func(self):
        """
        Function to be attached to self._wire (all EXCEPT n)
        """
        self.calc_res()
        self.calc_voltage()
        self.calc_power()
        self.calc_inductance()
        self.calc_time_constant()
        self.calc_weight()

    def trigger_all_coil_param_recalc_func(self):
        """
        Function to be attached to self._wire (all INCLUDING n)
        """
        self.calc_n()
        self.trigger_elec_coil_param_recalc_func()

    ## Define methods to be overridden by subclasses
    def calc_n(self):
        pass

    def calc_total_wire_length(self):
        pass

    def calc_res(self):
        pass

    def calc_voltage(self):
        pass

    def calc_power(self):
        pass

    def calc_inductance(self, **kwargs):
        pass

    def calc_time_constant(self, **kwargs):
        pass

    def calc_weight(self, **kwargs):
        pass
