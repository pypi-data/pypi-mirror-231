from __future__ import annotations

import numpy as np
import pandas as pd

from culib.utils.logs import get_local_logger
from culib.field.df_field import is_df_field_1d
from culib.field.validate import is_valid_pos_1d, is_valid_pos_3d, is_valid_axis


def get_fixed_axis_query_3d(axis: str, pos_x_mm, pos_y_mm, pos_z_mm) -> str:
    if is_valid_axis(axis, enable_raise=True):
        if axis == "x_mm":
            query_fixed_axis = f"y_mm == {pos_y_mm:.3f} and z_mm == {pos_z_mm:.3f}"
        elif axis == "y_mm":
            query_fixed_axis = f"x_mm == {pos_x_mm:.3f} and z_mm == {pos_z_mm:.3f}"
        elif axis == "z_mm":
            query_fixed_axis = f"x_mm == {pos_x_mm:.3f} and y_mm == {pos_y_mm:.3f}"
    return query_fixed_axis


def get_pos_1d_vs_pos_3d(axis: str, pos_3d_mm: tuple[float, float, float]) -> float:
    if is_valid_axis(axis, enable_raise=True) and is_valid_pos_3d(
        pos_3d_mm, enable_raise=True
    ):
        pos_x_mm = pos_3d_mm[0]
        pos_y_mm = pos_3d_mm[1]
        pos_z_mm = pos_3d_mm[2]
        if axis == "x_mm":
            pos_mm = pos_x_mm
        elif axis == "y_mm":
            pos_mm = pos_y_mm
        elif axis == "z_mm":
            pos_mm = pos_z_mm
        else:
            raise ValueError("axis not in ('x_mm', 'y_mm', 'z_mm')")
    return pos_mm


def get_field_at_pos(
    df_field: pd.DataFrame,
    Baxis: str,
    pos_mm: float | tuple[float, float, float],
    axis: str = None,
    **kwargs,
) -> float:
    """
    Get field component "Baxis" contained in df_field at "pos_mm" (on "axis" if pos_mm is 1D)

    Parameters
    ----------
    df_field : pd.DataFrame
        df containing the columns axis and Baxis
    Baxis : str
        Field axis name (i.e : 'By_coilA_mT')
    pos_mm: float or tuple[float, float, float]
        Position to look at in df_field. Can be specified :

        - as 1D : a single float, then you need to specify 'axis' parameter. Function will search pos in df_field[axis]
        - as 3D : a (float, float, float). You do not need to specify 'axis' parameter

    axis : str, optional
        Spatial axis name ('x_mm', 'y_mm' or 'z_mm'), needed only if pos_mm is 1D

    Returns
    -------
    B_pos_mT : float
        Magnetic field component Baxis in mT at given position

    Raises
    ------
    KeyError
        In case the field at position has not been found, or more than one line has been found
    ValueError
        In case pos_mm indicated as 1D but 'axis' not specified

    Examples
    --------
    >>> from culib import init_df_field, init_df_field_3d

    ## In 1D

    >>> df_field = init_df_field(axis_length_mm = 160, res_step_mm = 0.05)
    >>> get_field_at_pos(df_field, Baxis='Bx_total_mT', pos_mm=30.5, axis='x_mm') # will return Bx, which is 0 because no coils
    0

    ## In 3D

    >>> df_field_3d = init_df_field_3d(30, 1)
    >>> get_field_at_pos(df_field_3d, Baxis='Bx_total_mT', pos_mm=(-13, 12, -1)) # will return Bx at (-13, 12, -1), which is 0 because no coils
    0
    """

    log = get_local_logger("get_field_at_pos", **kwargs)

    is_pos_1d = is_valid_pos_1d(pos_mm, enable_raise=False, log=log)
    is_pos_3d = is_valid_pos_3d(pos_mm, enable_raise=False, log=log)

    if is_pos_1d:
        if axis is not None:
            query_wanted_pos = f"{axis} == {pos_mm:.2f}"
        else:
            err_msg = "pos_mm is 1D but 'axis' not specified"
            log.error(err_msg)
            raise ValueError(err_msg)
    elif is_pos_3d:
        query_wanted_pos = f"x_mm == {pos_mm[0]:.2f} and y_mm == {pos_mm[1]:.2f} and z_mm == {pos_mm[2]:.2f}"
    else:
        err_msg = f"pos_mm is either 1d nor 3d. Got {pos_mm}"
        log.error(err_msg)
        raise TypeError(err_msg)

    df_query = df_field.query(query_wanted_pos).reset_index()
    if len(df_query) == 1:
        try:
            B_pos_mT = df_query[Baxis][0]
        except KeyError:
            err_msg = f"'{Baxis}' column not existing in df_field"
            log.error(err_msg)
            raise KeyError(err_msg)
    elif len(df_query) == 0:
        err_msg = f"zero line found in df for query_wanted_pos : {query_wanted_pos}"
        log.error(err_msg)
        print(df_query.head())
        raise KeyError(err_msg)
    else:
        err_msg = f"more than one line found in df for query_wanted_pos : {query_wanted_pos}"  # fmt:skip
        log.error(err_msg)
        print(df_query.head())
        raise KeyError(err_msg)

    log.debug(f"succesfully got {Baxis} = {B_pos_mT:.3f} at pos_mm = {pos_mm}")

    return B_pos_mT


def get_field_homo_at_pos(
    df_field: pd.DataFrame,
    axis: str,
    Baxis: str,
    pos_mm: float | tuple[float, float, float],
    homo_region_mm: float = 0.5,
    **kwargs,
) -> float:
    """
    Calculate field homogeneity ratio from df_field at given position along "axis" and return it in %

    Parameters
    ----------
    df_field
        df containing the columns axis and Baxis
    axis : str
        axis name 'x_mm', 'y_mm' or 'z_mm'
    Baxis : str
        field axis name
    pos_mm: float or tuple[float, float, float]
        Position to look at in df_field. Can be specified :

        - as 1D : a single float. Function will search pos in df_field[axis]
        - as 3D : a (float, float, float).

    homo_region_mm : float, optional
        Region segment to check on 'axis' defined by [pos_mm-homo_region_mm, pos_mm+homo_region_mm].
        Default is 0.5mm.

    Returns
    -------
    homo_ratio_percent : float
        Field homogeneity ratio as percent

    Raises
    ------
    ValueError
        In case nothing found within the homo region

    Examples
    --------
    >>> import culib as cul
    >>> df_field = cul.init_df_field(axis_length_mm = 160, res_step_mm = 0.05)
    >>> my_right_helmholtz_coil = cul.CircularCoil(
    ...    axis='x_mm',
    ...    r_out_mm=50+5,
    ...    r_in_mm=50-5,
    ...    L_mm=15,
    ...    pos_mm=+50 / 2,
    ...    wire=cul.RoundWire(awg=22, t_insulation_mm=0.05),
    ...    cur_A=12)
    >>> df_field['Bx_right_coil_mT'] = my_right_helmholtz_coil.calc_field(df_field, ret_ser=True)
    >>> df_field = cul.calc_total_fields(df_field)
    >>> cul.get_field_homo_at_pos(df_field, axis='x_mm', Baxis='Bx_total_mT', pos_mm=30.5, homo_region_mm=0.5) # Will return homogeneity value in % already
    0.6244405971027318

    ## In 3D

    >>> df_field_3d = cul.init_df_field_3d(30, 1)
    >>> df_field_3d = my_right_helmholtz_coil.calc_field_3d(df_field_3d)
    >>> df_field_3d = cul.calc_total_fields(df_field_3d)
    >>> pos_mm = (3, -12, 1)
    >>> cul.get_field_homo_at_pos(df_field_3d, axis='z_mm', Baxis='Bx_total_mT', pos_mm=pos_mm, homo_region_mm=5) # Will return homogeneity value in % already
    0.3444299098113213
    """
    log = get_local_logger("get_field_homo_at_pos", **kwargs)

    # Detect if df_field is 1d or 3d in order to adapt query_homo_region
    is_df_1d = is_df_field_1d(df_field, enable_raise=False, log=log)

    is_pos_1d = is_valid_pos_1d(pos_mm, enable_raise=False, log=log)
    is_pos_3d = is_valid_pos_3d(pos_mm, enable_raise=False, log=log)

    # Manage 3D pos
    if is_pos_1d:
        pos_axis_mm = pos_mm
    elif is_pos_3d:
        pos_x_mm = pos_mm[0]
        pos_y_mm = pos_mm[1]
        pos_z_mm = pos_mm[2]
        query_fixed_axis = get_fixed_axis_query_3d(axis, pos_x_mm, pos_y_mm, pos_z_mm)
        pos_axis_mm = get_pos_1d_vs_pos_3d(axis, pos_mm)
    else:
        err_msg = f"pos_mm is either a num nor a tuple of 3 num. Got pos_mm={pos_mm}"
        log.error(err_msg)
        raise TypeError(err_msg)

    # Filter df_field to keep region of interest
    ## Prepare query
    query_homo_region = f"{axis} >= {pos_axis_mm-homo_region_mm:.3f} and {axis} <= {pos_axis_mm+homo_region_mm:.2f}"  # fmt: skip
    ## Case df 1d
    if is_df_1d:
        list_col_to_keep = [axis, Baxis]
        df_homo = df_field[list_col_to_keep]
    ## Case df 3d (must then provide pos_mm in 3D)
    elif is_pos_3d:
        query_homo_region += " and " + query_fixed_axis
        list_col_to_keep = ["x_mm", "y_mm", "z_mm", Baxis]
        df_homo = df_field[list_col_to_keep]
    else:
        err_msg = f"provided 3D df_field but did not specified pos_mm as 3D. Got pos_mm={pos_mm}"
        log.error(err_msg)
        raise TypeError(err_msg)
    ## Apply query to df_homo
    log_msg = f"will check Baxis='{Baxis}' on axis='{axis}', in region of {pos_axis_mm:.2f} +/- {homo_region_mm:.2f} mm"  # fmt: skip
    if is_pos_3d:
        log_msg += f" (center pos_mm = ({pos_x_mm:.2f}, {pos_y_mm:.2f}, {pos_z_mm:.2f})"
    log.info(log_msg)
    log.debug(f"query_homo_region = '{query_homo_region}'")
    df_homo = df_homo.query(query_homo_region).reset_index()

    # Check df_homo size
    if len(df_homo) == 0:
        err_msg = f"empty df found after query_homo_region = '{query_homo_region}'"
        log.error(err_msg)
        raise ValueError(err_msg)
    else:
        log.info(f"len(df_homo) = {len(df_homo)}")

    # Get B values
    B_pos_mT = get_field_at_pos(
        df_field, Baxis=Baxis, pos_mm=pos_mm, axis=axis, **kwargs
    )
    B_min_mT = min(df_homo[Baxis])
    B_max_mT = max(df_homo[Baxis])
    log.info(f'B_pos_mT = {B_pos_mT:.3f}, B_min_mT = {B_min_mT:.3f}, B_max_mT = {B_max_mT:.3f}')  # fmt: skip

    if not np.isclose(B_pos_mT, 0, rtol=1e-2):
        homo_ratio_percent = (B_max_mT - B_min_mT) / B_pos_mT * 100
    elif not np.isclose(B_max_mT, -B_min_mT, rtol=1e-3):
        warn_msg = "B_pos_mT is 0, defining homo as diff(max-min) / avg(max-min)"
        log.warning(warn_msg)
        homo_ratio_percent = 2 * (B_max_mT - B_min_mT) / (B_max_mT + B_min_mT) * 100
    elif not np.isclose(B_max_mT, 0, rtol=1e-1):
        warn_msg = "B_pos is 0 and Bmax = -Bmin, can't define homo ratio. Returning nan"
        log.warning(warn_msg)
        homo_ratio_percent = np.nan  # (B_max_mT - B_min_mT) / (B_max_mT) * 100
    else:
        err_msg = "B_pos, B_min and B_max are 0, can't define homo ratio. Returning nan"
        log.error(err_msg)
        homo_ratio_percent = np.nan

    log.info(f"homo_ratio_percent = {abs(homo_ratio_percent):.3f} % for {Baxis}=f({axis}) in region of pos_mm = {pos_axis_mm:.2f} +/- {homo_region_mm:.2f} mm")  # fmt: skip

    return abs(homo_ratio_percent)


def rescale_current_for_field(
    B_wanted_mT: float,
    cur_A: float,
    B_current_mT: float = None,
    df_field: pd.DataFrame = None,
    axis: str = None,
    Baxis: str = None,
    pos_mm: float | tuple[float, float, float] = None,
    **kwargs,
) -> float:
    """
    Calculate current required for reaching wanted field B_wanted_mT from a baseline cur_A given in argument.
    If B_current_mT is given, it will scale versus B_current_mT.
    Alternatively, if df_field, axis, Baxis and pos_mm are given, it will get current field at position and then apply cross product to return the rescaled current.

    Parameters
    ----------
    df_field
        df containing the columns axis and Baxis
    axis : str
        axis name 'x_mm', 'y_mm' or 'z_mm'
    Baxis : str
        field axis name
    pos_mm: float or tuple[float, float, float]
        Position to look at in df_field. Can be specified :

        - as 1D : a single float. Function will search pos in df_field[axis]
        - as 3D : a (float, float, float).
    B_wanted_mT : float
        Field target in mT
    cur_A : float
        Current currently applied to be rescaled for reaching B_wanted_mT in A

    Returns
    -------
    rescaled_current_A : float
        Rescaled current in A for reaching B_wanted_mT at pos

    Examples
    --------
    >>> import culib as cul
    >>> my_coil = cul.CircularCoil(
    ...    axis='x_mm',
    ...    r_out_mm=50+5,
    ...    r_in_mm=50-5,
    ...    L_mm=15,
    ...    pos_mm=+50 / 2,
    ...    wire=cul.RoundWire(awg=22, t_insulation_mm=0.05),
    ...    cur_A=12,
    ... )
    >>> df_field = cul.init_df_field(axis_length_mm=160, res_step_mm=0.05)
    >>> df_field = my_coil.calc_field(df_field)
    >>> df_field = cul.calc_total_fields(df_field)
    >>> Bx_at_pos = get_field_at_pos(df_field, axis='x_mm', Baxis='Bx_total_mT', pos_mm=30.5)
    >>> print(round(Bx_at_pos, 4))
    38.1095

    ## Rescale current to get 15mT at pos_mm

    >>> my_coil.cur_A = cul.rescale_current_for_field(df_field=df_field, axis='x_mm', Baxis='Bx_total_mT', pos_mm=30.5, B_wanted_mT=15, cur_A=my_coil.cur_A)
    >>> print(my_coil.cur_A)
    4.72322861694687
    >>> df_field = my_coil.calc_field(df_field)
    >>> df_field = cul.calc_total_fields(df_field)
    >>> Bx_at_pos = get_field_at_pos(df_field, axis='x_mm', Baxis='Bx_total_mT', pos_mm=30.5)
    >>> print(round(Bx_at_pos, 4))
    15.0

    ## In 3D

    >>> df_field_3d = cul.init_df_field_3d(30, 1)
    >>> df_field_3d = my_coil.calc_field_3d(df_field_3d)
    >>> df_field_3d = cul.calc_total_fields(df_field_3d)
    >>> pos_mm = (12, 0, -5)
    >>> Bx_at_pos = get_field_at_pos(df_field_3d, axis='x_mm', Baxis='Bx_total_mT', pos_mm=pos_mm)
    >>> print(round(Bx_at_pos, 4))
    13.8396
    >>> my_coil.cur_A = cul.rescale_current_for_field(df_field=df_field_3d, axis='x_mm', Baxis='Bx_total_mT', pos_mm=pos_mm, B_wanted_mT=15, cur_A=my_coil.cur_A)
    >>> df_field_3d = my_coil.calc_field_3d(df_field_3d)
    >>> df_field_3d = cul.calc_total_fields(df_field_3d)
    >>> Bx_at_pos = get_field_at_pos(df_field_3d, axis='x_mm', Baxis='Bx_total_mT', pos_mm=pos_mm)
    >>> print(round(Bx_at_pos, 4))
    15.0

    """
    log = get_local_logger("rescale_current_for_field", **kwargs)

    # Get field at pos
    if B_current_mT is not None:
        B_pos_mT = B_current_mT
    elif df_field is not None:
        if Baxis is not None and pos_mm is not None:
            is_pos_1d = is_valid_pos_1d(pos_mm)
            is_pos_3d = is_valid_pos_3d(pos_mm)
            if is_pos_3d or (is_pos_1d and axis is not None):
                B_pos_mT = get_field_at_pos(
                    df_field, Baxis=Baxis, pos_mm=pos_mm, axis=axis, **kwargs
                )
            else:
                err_msg = f"pos_mm is 1D but 'axis' not specified or pos_mm is not valid 3D. Got pos_mm={pos_mm}"  # fmt: skip
                log.error(err_msg)
                raise ValueError(err_msg)
        else:
            err_msg = "specified df_field to retrieve current field in df_field, but missing 'Baxis' or 'pos_mm' or 'axis'"  # fmt: skip
            log.error(err_msg)
            raise ValueError(err_msg)
    else:
        err_msg = "none of B_current_mT or df_field specified, need to give one or another"  # fmt: skip
        log.error(err_msg)
        raise ValueError(err_msg)

    # Calc rescale current
    rescaled_current_A = cur_A * B_wanted_mT / B_pos_mT

    return rescaled_current_A


def get_axes_from_list(list_axes: list[str], **kwargs) -> str:
    """
    Parameters
    ----------
    list_axes : list[str]

    Returns
    -------
    ret_str_axes : str
        One concatenated string with different axis in list_axis (i.e : "x", "yz", "xyz"...).
        Returns empty string if no valid axis given.

    Examples
    --------
    >>> Baxis = ["Bx_total_mT", "By_total_mT", "Bz_total_mT"]
    >>> get_axes_from_list(Baxis)
    'xyz'

    >>> Baxis = ["By_A1_mT", "By_A2_mT", "By_total_mT"]
    >>> get_axes_from_list(Baxis)
    'y'

    >>> Baxis = ["x_mm", "y_mm", "z_mm"]
    >>> get_axes_from_list(Baxis)
    'xyz'

    >>> list_axes = ["hello", "A1"]
    >>> get_axes_from_list(list_axes)
    ''
    """
    log = get_local_logger("get_axes_from_list", **kwargs)

    valid_axis_letters = ("x", "y", "z")
    ret_str_axes = ""

    # Id if fields or geom axes
    list_geom = [el for el in list_axes if el.endswith("_mm")]
    list_field = [el for el in list_axes if el.endswith("_mT")]

    if list_geom == [] and list_field != []:
        # Got list of field axes
        for B in list_field:
            axis = B[1]
            if axis in valid_axis_letters:
                if axis not in ret_str_axes:
                    ret_str_axes += axis
            else:
                err_msg = f"got unknown axis (not in {valid_axis_letters}). Got {axis}"
                log.warning(err_msg)
    elif list_geom != [] and list_field == []:
        # Got list of geom axes
        for ax in list_geom:
            axis = ax[0]
            if axis in valid_axis_letters:
                if axis not in ret_str_axes:
                    ret_str_axes += axis
            else:
                err_msg = f"got unknown axis (not in {valid_axis_letters}). Got {axis}"
                log.warning(err_msg)
    elif list_geom != [] and list_field != []:
        err_msg = f"got invalid list (mixed fields and geom axis). Got {list_axes}"
        log.warning(err_msg)
    elif list_geom == [] and list_field == []:
        err_msg = f"got invalid list (neither fields nor geom axis). Got {list_axes}"
        log.warning(err_msg)
    else:
        err_msg = f"unexpected issue. Got {list_axes}"
        log.error(err_msg)

    ret_str_axes = "".join(sorted(ret_str_axes))

    return ret_str_axes
