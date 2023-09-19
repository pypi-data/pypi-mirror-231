from __future__ import annotations

from logging import Logger

import numpy as np

from culib.utils.logs import get_local_logger


def is_valid_pos_1d(pos_mm, enable_raise: bool = False, log: Logger = None) -> bool:
    """
    Check if pos_mm is a single float (so an only 1d pos)

    Examples
    --------
    >>> is_valid_pos_1d(12)
    True
    >>> is_valid_pos_1d((-2, 51, 12))
    False
    """
    accepted_pos_mm_types = (int, np.int32, np.int64, float, np.float32, np.float64)
    is_valid = isinstance(pos_mm, accepted_pos_mm_types)
    if enable_raise and not is_valid:
        if log is None:
            log = get_local_logger("is_valid_pos_1d")
        err_msg = f"pos_mm is not a valid 1d. Got pos_mm={pos_mm}"
        log.error(err_msg)
        raise TypeError(err_msg)
    return is_valid


def is_valid_pos_3d(pos_mm, enable_raise: bool = True, log: Logger = None) -> bool:
    """
    Check if pos_mm is a tuple of 3 floats (so a valid 3d pos)

    Examples
    --------
    >>> is_valid_pos_3d(12)
    False
    >>> is_valid_pos_3d((-2, 51, 12))
    True
    """
    is_valid = False
    if log is None:
        log = get_local_logger("is_valid_pos_3d")
    if isinstance(pos_mm, tuple):
        # Validate length is 3 positions
        if len(pos_mm) != 3:
            if enable_raise:
                err_msg = f"pos_mm specified as Tuple, but does not have 3 positions. Correct format should be (pos_x_mm, pos_y_mm, pos_z_mm). Got {pos_mm}"
                log.error(err_msg)
                raise ValueError(err_msg)
            else:
                return False
        # Validate type
        for el in pos_mm:
            if not is_valid_pos_1d(el):
                if enable_raise:
                    err_msg = f"got one comp of pos_mm not numeric : {el}"
                    log.error(err_msg)
                    raise TypeError(err_msg)
                else:
                    return False
        is_valid = True

    return is_valid


def is_valid_axis(axis: str, enable_raise: bool = True, log: Logger = None) -> bool:
    """
    Check if axis is correct type and matching 'x_mm', 'y_mm' or 'z_mm'.

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
    is_valid = False
    list_valid_axis = ("x_mm", "y_mm", "z_mm")
    if log is None:
        log = get_local_logger("is_valid_axis")
    if isinstance(axis, str):
        if axis in list_valid_axis:
            is_valid = True
        else:
            err_msg = f"axis is not in {list_valid_axis}. Got axis={axis}"
            log.error(err_msg)
            if enable_raise:
                raise ValueError(err_msg)
    else:
        err_msg = f"axis specified is not a string. Type must be str. Got axis={axis}"
        log.error(err_msg)
        if enable_raise:
            raise TypeError(err_msg)

    return is_valid
