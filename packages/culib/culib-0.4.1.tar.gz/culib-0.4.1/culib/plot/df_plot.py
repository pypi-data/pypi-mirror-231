from __future__ import annotations

import pandas as pd

from culib.utils.logs import get_local_logger
from culib.field.df_field import is_df_field_1d, is_df_field_3d
from culib.field.validate import is_valid_pos_1d, is_valid_pos_3d
from culib.field.getters import get_fixed_axis_query_3d, get_pos_1d_vs_pos_3d
from culib.plot.settings import DEFAULT_NB_PLOT_SAMPLES


def prepare_df_plot_field(
    df_field: pd.DataFrame,
    axis: str,
    Baxis: str | list,
    is_zoom_on_pos: bool = False,
    pos_mm: float | tuple[float, float, float] = None,
    homo_region_mm: float = None,
    nb_plot_samples: int = None,
    **kwargs,
) -> pd.DataFrame:
    log = get_local_logger("prepare_df_plot_field", **kwargs)

    # Detect if 1d or 3d in order to adapt queries
    is_pos_1d = is_valid_pos_1d(pos_mm, enable_raise=False)
    is_pos_3d = is_valid_pos_3d(pos_mm, enable_raise=False)
    is_df_1d = is_df_field_1d(df_field, enable_raise=False)
    is_df_3d = is_df_field_3d(df_field, enable_raise=False)

    # Manage 1D or 3D for pos and df
    query_fixed_axis = ""
    if is_pos_1d and is_df_1d:
        pos_axis_mm = pos_mm
    elif is_pos_3d and is_df_1d:
        err_msg = "pos_mm is 3d but df is 1d. Must specify pos_mm as 1d on 'axis'"
        log.error(err_msg)
        raise TypeError(err_msg)
    elif is_pos_3d and is_df_3d:
        pos_x_mm = pos_mm[0]
        pos_y_mm = pos_mm[1]
        pos_z_mm = pos_mm[2]
        pos_axis_mm = get_pos_1d_vs_pos_3d(axis, pos_mm)
        query_fixed_axis = get_fixed_axis_query_3d(axis, pos_x_mm, pos_y_mm, pos_z_mm)
    elif is_df_3d:  # and is_pos_1d # To account for pos_mm = None
        if axis == "x_mm":
            pos_x_mm = pos_axis_mm = pos_mm
            pos_y_mm = 0
            pos_z_mm = 0
        elif axis == "y_mm":
            pos_x_mm = 0
            pos_y_mm = pos_axis_mm = pos_mm
            pos_z_mm = 0
        elif axis == "z_mm":
            pos_x_mm = 0
            pos_y_mm = 0
            pos_z_mm = pos_axis_mm = pos_mm
        else:
            err_msg = f"unknown axis (should be 'x_mm', 'y_mm' or 'z_mm'. Got {axis}"
            log.error(err_msg)
            raise ValueError(err_msg)
        query_fixed_axis = get_fixed_axis_query_3d(axis, pos_x_mm, pos_y_mm, pos_z_mm)

    # Keep only useful portion of df
    ## Check if one or multiple Baxis
    if isinstance(Baxis, str):
        Baxis = [Baxis]
    ## Check if df_field 1d or 3d
    if is_df_1d:
        list_axis_to_keep = [axis]
    elif is_df_3d:
        list_axis_to_keep = ["x_mm", "y_mm", "z_mm"]
    else:
        err_msg = "df_field either valid 1D nor valid 3D"
        log.error(err_msg)
        raise TypeError(err_msg)

    list_col_to_keep = list_axis_to_keep + Baxis
    df_plot = df_field[list_col_to_keep]

    # Default nb_plot_sample
    if nb_plot_samples is None:
        nb_plot_samples = DEFAULT_NB_PLOT_SAMPLES
        log.debug(f"nb_plot_samples set to default = {nb_plot_samples}")

    # Manage Zoom case
    if is_zoom_on_pos:
        if pos_mm is None or homo_region_mm is None:
            err_msg = "'Zoom on pos' enabled but pos_mm and/or homo_region_mm not specified"  # fmt:skip
            log.error(err_msg)
            raise TypeError(err_msg)
        else:
            # Prepare queries to keep only useful positions (based on 1D or 3D)
            query_homo_region = f"{axis} >= {pos_axis_mm-homo_region_mm:.3f} and {axis} <= {pos_axis_mm+homo_region_mm:.3f}"
            if query_fixed_axis != "":
                query_homo_region += " and " + query_fixed_axis
            log_msg = f"'Zoom on pos' enabled, will plot at pos_mm = {pos_axis_mm:.2f} +/- {homo_region_mm:.2f} mm"
            if is_pos_3d:
                log_msg += f" (center pos_mm =({pos_x_mm:.2f}, {pos_y_mm:.2f}, {pos_z_mm:.2f}))"  # fmt: skip
            log.info(log_msg)

            # Apply query to keep only useful positions
            log.debug(f"query_homo_region = '{query_homo_region}'")
            df_plot = df_plot.query(query_homo_region).reset_index()
            # Check plot size
            if len(df_plot) == 0:
                err_msg = f"Empty df found after query_homo_region = '{query_homo_region}'"  # fmt:skip
                log.error(err_msg)
                raise KeyError(err_msg)
    else:
        log.info("'Zoom on pos' disabled, will plot full axis")
        if is_df_3d:
            df_plot = df_plot.query(query_fixed_axis).reset_index()
        if len(df_plot) == 0:
            err_msg = f"Empty df found after query_fixed_axis = '{query_fixed_axis}'"  # fmt:skip
            log.error(err_msg)
            raise KeyError(err_msg)

    # Check size
    # TODO (prio 2): use evenly spaced points instead of sample
    if len(df_plot) > nb_plot_samples:
        warn_msg = f"Length of df_plot ({len(df_plot)}) above max nb_plot_samples ({nb_plot_samples}), will reduce size via random .sample({nb_plot_samples}) method"  # fmt: skip
        log.warning(warn_msg)
        df_plot_sample = df_plot.sample(n=nb_plot_samples)
        if pos_mm is not None:
            query_pos = f"{axis} == {pos_axis_mm:.3f}"
            if is_pos_3d:
                query_pos += query_fixed_axis
            df_plot_pos_mm = df_plot.query(query_pos)
            df_plot = pd.concat(
                [df_plot_pos_mm, df_plot_sample]
            ).drop_duplicates()  # To make sure line with pos_mm is in df_plot

    return df_plot
