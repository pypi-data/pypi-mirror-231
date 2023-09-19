from __future__ import annotations

from logging import Logger

import pandas as pd
import numpy as np

from culib.utils.logs import get_local_logger

DEFAULT_1D_AXIS_LENGTH_MM = 160
DEFAULT_1D_RES_STEP_MM = 0.05

DEFAULT_3D_AXIS_LENGTH_MM = 100
DEFAULT_3D_RES_STEP_MM = 1


def init_df_field(
    axis_length_mm: float = DEFAULT_1D_AXIS_LENGTH_MM,
    res_step_mm: float = DEFAULT_1D_RES_STEP_MM,
    **kwargs,
) -> pd.DataFrame:
    """
    Prepare an empty df with axis columns and arrays for field calculation.
    Will prepare 3 x 1D axis (not a full 3D mesh).

    Parameters
    ----------
    axis_length_mm : float, optional
        Total length of the axis in mm. Axis will be between [-axis_length_mm/2, +axis_length_mm/2], in order to contain zero. Default = 160
    res_step_mm : float, optional
        Resolution step wanted between 2 points in mm. Default = 0.05

    Returns
    -------
    df_field : pd.DataFrame
        Dataframe containing 3 columns with spatial axis "x_mm", "y_mm" and "z_mm" + 3 columns with B field components "Bx_total_mT", "By_total_mT" and "Bz_total_mT", initialized at 0.
        Shape = (int(axis_length_mm/res_step_mm)+1, 6)

    Examples
    --------
    ## Get df_field with default values

    >>> df_field = init_df_field()

    ## Specify with custom values

    >>> df_field = init_df_field(axis_length_mm = 160, res_step_mm = 0.05)

    """
    # log = get_local_logger('init_df_field', **kwargs)

    res_axis = int(axis_length_mm / res_step_mm) + 1

    df_field = pd.DataFrame()
    df_field["x_mm"] = np.linspace(
        start=-axis_length_mm / 2, stop=axis_length_mm / 2, num=res_axis
    )
    df_field["y_mm"] = np.linspace(
        start=-axis_length_mm / 2, stop=axis_length_mm / 2, num=res_axis
    )
    df_field["z_mm"] = np.linspace(
        start=-axis_length_mm / 2, stop=axis_length_mm / 2, num=res_axis
    )

    df_field["Bx_total_mT"] = 0
    df_field["By_total_mT"] = 0
    df_field["Bz_total_mT"] = 0

    return df_field


def init_df_field_3d(
    axis_length_mm: float = DEFAULT_3D_AXIS_LENGTH_MM,
    res_step_mm: float = DEFAULT_3D_RES_STEP_MM,
) -> pd.DataFrame:
    """
    Prepare an empty df with axis columns and arrays for field calculation.
    Will prepare a full 3D mesh.

    WARNING : be careful with small res_step_mm, size of df is function of (length/res)^3 !

    Parameters
    ----------
    axis_length_mm : float, optional
        Total length of the axis in mm. Axis will be between [-axis_length_mm/2, +axis_length_mm/2], in order to contain zero. Default = 100
    res_step_mm : float, optional
        Resolution step wanted between 2 points in mm. Default = 1

    Returns
    -------
    df_field : pd.DataFrame
        Dataframe containing 3 columns with spatial axis x_mm, y_mm and z_mm + 3 columns with B field components Bx_total_mT, By_total_mT and Bz_total_mT, initialized at 0.
        Shape = ((int(axis_length_mm/res_step_mm)+1)**3, 6)

    Examples
    --------
    ## Get df_field with default values

    >>> df_field_3d = init_df_field_3d()
    >>> df_field_3d.shape
    (1030301, 6)

    ## Specify with custom values (and beware of HUGE size of df for small step !)

    >>> df_field_3d = init_df_field_3d(res_step_mm = 0.5)
    >>> df_field_3d.shape
    (8120601, 6)

    -------

    """
    res_axis = int(axis_length_mm / res_step_mm) + 1
    ser_axis = np.linspace(
        start=-axis_length_mm / 2, stop=axis_length_mm / 2, num=res_axis
    )

    df_x = pd.DataFrame(ser_axis, columns=["x_mm"])
    df_y = pd.DataFrame(ser_axis, columns=["y_mm"])
    df_z = pd.DataFrame(ser_axis, columns=["z_mm"])

    df_x["Bx_total_mT"] = 0
    df_y["Bx_total_mT"] = 0
    df_z["Bx_total_mT"] = 0

    df_xy = pd.merge(df_x, df_y, on="Bx_total_mT", how="outer")
    df_field = pd.merge(df_xy, df_z, on="Bx_total_mT", how="outer")

    df_field["By_total_mT"] = 0
    df_field["Bz_total_mT"] = 0

    # Reorder columns
    list_col = ["x_mm", "y_mm", "z_mm", "Bx_total_mT", "By_total_mT", "Bz_total_mT"]
    df_field = df_field[list_col]

    return df_field


def calc_total_fields(df_field: pd.DataFrame) -> pd.DataFrame:
    """
    Automatically recalculates Bx_total_mT, By_total_mT and Bz_total_mT from sum of all applicable columns
    (field superposition theorem)

    Parameters
    ----------
    df_field : pd.DataFrame
        Dataframe containing 3 columns with spatial axis x_mm, y_mm and z_mm + field components

    Returns
    -------
    df_field : pd.DataFrame
        Updated df_field with Bx_total_mT, By_total_mT and Bz_total_mT recalculated from all applicable columns

    Examples
    --------
    >>> from culib import get_field_at_pos, CircularCoil, Wire
    >>> df_field = init_df_field(axis_length_mm=250, res_step_mm=0.05)
    >>> G_coils_mm = 60  # Gap between coils centers in mm
    >>> dut_pos_mm = 30  # DUT position
    >>> hall5_coils_param = {
    ...     'r_out_mm': 14,
    ...     'r_in_mm': 5,
    ...     'L_mm': 30,
    ...     'n': 348,
    ...     'cur_A': 2.7,
    ...     'wire': Wire(d_in_mm=0.812),
    ... }
    >>> left_coil = CircularCoil(
    ...     axis='y_mm',
    ...     pos_mm=-G_coils_mm,
    ...     **hall5_coils_param)
    >>> df_field = left_coil.calc_field(df_field)
    >>> mid_coil = CircularCoil(
    ...    axis='y_mm',
    ...    pos_mm=0,
    ...    **hall5_coils_param)
    >>> df_field = mid_coil.calc_field(df_field)
    >>> right_coil = CircularCoil(
    ...     axis='y_mm',
    ...     pos_mm=+G_coils_mm,
    ...     **hall5_coils_param)
    >>> df_field = right_coil.calc_field(df_field)
    >>> df_field = calc_total_fields(df_field) # Will make the sum of df_field['By_left_coil_mT'] + df_field['By_mid_coil_mT'] + df_field['By_right_coil_mT']
    >>> get_field_at_pos(df_field, axis='y_mm', Baxis='By_total_mT', pos_mm=dut_pos_mm)
    5.334750390760416
    """

    # log = get_local_logger('init_df_field', **kwargs)
    list_Bx_fields_to_sum = [
        c
        for c in df_field.columns
        if (c.startswith("Bx_") and c != "Bx_total_mT" and c != "Bx_mT")
    ]
    list_By_fields_to_sum = [
        c
        for c in df_field.columns
        if (c.startswith("By_") and c != "By_total_mT" and c != "By_mT")
    ]
    list_Bz_fields_to_sum = [
        c
        for c in df_field.columns
        if (c.startswith("Bz_") and c != "Bz_total_mT" and c != "Bz_mT")
    ]

    if len(list_Bx_fields_to_sum) > 0:
        df_field["Bx_total_mT"] = 0
        for c in list_Bx_fields_to_sum:
            df_field["Bx_total_mT"] += df_field[c]

    if len(list_By_fields_to_sum) > 0:
        df_field["By_total_mT"] = 0
        for c in list_By_fields_to_sum:
            df_field["By_total_mT"] += df_field[c]

    if len(list_Bz_fields_to_sum) > 0:
        df_field["Bz_total_mT"] = 0
        for c in list_Bz_fields_to_sum:
            df_field["Bz_total_mT"] += df_field[c]

    return df_field


def is_df_field_1d(
    df_field: pd.DataFrame, enable_raise: bool = False, log: Logger = None
) -> bool:
    """
    >>> import culib as cul
    >>> df_1d = cul.init_df_field()
    >>> is_df_field_1d(df_1d)
    True
    >>> df_3d = cul.init_df_field_3d(10,1)
    >>> is_df_field_1d(df_3d)
    False
    """
    set_df_columns = {el for el in df_field.columns}
    is_all_axis_inside = {"x_mm", "y_mm", "z_mm"}.issubset(set_df_columns)

    if is_all_axis_inside:
        is_all_axis_equal = (df_field["x_mm"] == df_field["y_mm"]).all()
        if not is_all_axis_equal and enable_raise:
            if log is None:
                log = get_local_logger("is_df_field_1d")
            err_msg = "df_field is not a valid 1d"
            log.error(err_msg)
            raise TypeError(err_msg)
        return is_all_axis_equal
    else:
        return True


def is_df_field_3d(
    df_field: pd.DataFrame, enable_raise: bool = False, log: Logger = None
) -> bool:
    """
    >>> import culib as cul
    >>> df_1d = cul.init_df_field()
    >>> is_df_field_3d(df_1d)
    False
    >>> df_3d = cul.init_df_field_3d(10,1)
    >>> is_df_field_3d(df_3d)
    True
    """
    set_df_columns = {el for el in df_field.columns}
    is_all_axis_inside = {"x_mm", "y_mm", "z_mm"}.issubset(set_df_columns)

    if is_all_axis_inside:
        is_all_axis_equal = (df_field["x_mm"] == df_field["y_mm"]).all()
        if is_all_axis_equal and enable_raise:
            if log is None:
                log = get_local_logger("is_df_field_3d")
            err_msg = "df_field is not a valid 3d"
            log.error(err_msg)
            raise TypeError(err_msg)
        return not is_all_axis_equal
    else:
        return False
