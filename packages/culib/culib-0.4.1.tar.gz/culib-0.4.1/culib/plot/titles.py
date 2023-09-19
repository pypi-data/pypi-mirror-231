from __future__ import annotations

import numpy as np

from culib.field.validate import is_valid_pos_3d
from culib.field.getters import (
    get_axes_from_list,
    get_pos_1d_vs_pos_3d,
    get_fixed_axis_query_3d,
)


def format_query_fixed_axis(query_fixed_axis: str) -> str:
    """
    Should return "(y_mm, z_mm) = (12, 53.57)" from query_fixed_axis like :
    "y_mm == 12 and z_mm == 53.57"

    Examples
    --------
    >>> query_fixed_axis = "y_mm == 12 and z_mm == 53.57"
    >>> format_query_fixed_axis(query_fixed_axis)
    '(y_mm, z_mm) = (12.0, 53.57)'
    """
    subqueries = query_fixed_axis.split(" and ")
    axis1 = subqueries[0][0:4]
    val1 = float(subqueries[0].split(" == ")[1])
    axis2 = subqueries[1][0:4]
    val2 = float(subqueries[1].split(" == ")[1])
    ret_str = f"({axis1}, {axis2}) = ({val1}, {val2})"
    return ret_str


def prepare_graphtitles(
    axis: str,
    is_zoom_on_pos: bool,
    pos_mm: float,
    homo_region_mm: float,
    dict_titles: dict = {},
    **kwargs,
) -> list[str]:
    list_graphtitles = []
    ## General line
    if "graphtitle" in kwargs.keys():
        line = kwargs["graphtitle"]
        list_graphtitles.append(line)
    elif "graphtitle" in dict_titles.keys():
        line = dict_titles["graphtitle"]
        list_graphtitles.append(line)
    ## Line Full axis/Zoom
    if is_valid_pos_3d(pos_mm):
        pos_mm = get_pos_1d_vs_pos_3d(axis, pos_mm)

    if is_zoom_on_pos:
        line = f"Zoom on region pos_mm = {pos_mm:.2f} +/- {homo_region_mm:.2f} mm"
    else:
        line = f"Full line {axis[0]}"
    list_graphtitles.append(line)
    ## Manage dict_titles
    line = ""
    for key in dict_titles.keys():
        if key.lower() != "graphtitle":
            option_name = key
            option_value = dict_titles[key]
            if isinstance(option_value, (float, np.float64)):
                option_value = round(option_value, 2)
            optional_string = f"{option_name} = {option_value}, "
            line += optional_string
    if line != "":
        line = line[:-2]  # Remove ", "
        list_graphtitles.append(line)

    ## Line end with ''
    list_graphtitles.append("")
    return list_graphtitles


def prepare_graphsubtitles(
    axis: str,
    Baxis: list[str],
    Baxis_column_homo: str,
    homo_percent: float = None,
    dict_subtitles: dict = {},
    pos_mm: float | tuple[float, float, float] = None,
    **kwargs,
) -> list[str]:
    list_graphsubtitles = []

    ## General line
    if "graphsubtitle" in kwargs.keys():
        line = kwargs["graphsubtitle"]
        list_graphsubtitles.append(line)
    elif "graphtitle" in dict_subtitles.keys():
        line = dict_subtitles["graphsubtitle"]
        list_graphsubtitles.append(line)

    ## Line Baxis = f(axis)
    B_axis_letter = get_axes_from_list(Baxis)
    line = f"B{B_axis_letter} = f({axis[0]})"
    if is_valid_pos_3d(pos_mm):
        pos_x_mm = pos_mm[0]
        pos_y_mm = pos_mm[1]
        pos_z_mm = pos_mm[2]
        query_fixed_axis = get_fixed_axis_query_3d(axis, pos_x_mm, pos_y_mm, pos_z_mm)
        fixed_axis = format_query_fixed_axis(query_fixed_axis)
        line += " at fixed " + fixed_axis
    list_graphsubtitles.append(line)

    ## Line for homogeneity
    if homo_percent:
        line = f"Field discrepancy ratio = {homo_percent:.2f} % for {Baxis_column_homo}"  # FHM : Field Homogeneity Metric
        list_graphsubtitles.append(line)

    ## Manage dict_subtitles
    line = ""
    for key in dict_subtitles.keys():
        if key.lower() != "graphsubtitle":
            option_name = key
            option_value = dict_subtitles[key]
            if isinstance(option_value, (float, np.float64)):
                option_value = round(option_value, 2)
            optional_string = f"{option_name} = {option_value}, "
            line += optional_string
    if line != "":
        line = line[:-2]  # Remove ", "
        list_graphsubtitles.append(line)

    return list_graphsubtitles
