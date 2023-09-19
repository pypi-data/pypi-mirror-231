from __future__ import annotations

from pathlib import Path
from typing import Any

import altair as alt
import pandas as pd

from culib.utils.logs import get_local_logger
from culib.field.getters import get_field_homo_at_pos
from culib.plot.charts import generate_chart_fields, generate_chart_rules_and_labels
from culib.plot.df_plot import prepare_df_plot_field
from culib.plot.save import save_chart
from culib.plot.titles import prepare_graphtitles, prepare_graphsubtitles
from culib.plot.settings import DEFAULT_NB_PLOT_SAMPLES

DEFAULT_POS_MM = 0.0
DEFAULT_HOMO_REGION_MM = 0.5


def plot_field(
    df_field: pd.DataFrame,
    axis: str,
    Baxis: str | list,
    is_zoom_on_pos: bool = False,
    pos_mm: float | tuple[float, float, float] = None,
    homo_region_mm: float = None,
    Baxis_homo: str = None,
    dezoom_factor: float = 0.01,
    dict_titles: dict[str, Any] = {},
    dict_subtitles: dict[str, Any] = {},
    dict_pos_mm_vs_label: dict = None,
    is_save: bool = False,
    save_filename: str = None,
    savepath_png: Path | str = None,
    savepath_html: Path | str = None,
    save_scale_factor: float = 1.0,
    nb_plot_samples: int = DEFAULT_NB_PLOT_SAMPLES,
    **kwargs,
) -> alt.Chart:
    """
    Plot Bfield Baxis=f(axis) from df_field.

    If is_zoom_on_pos set to True, will plot between x-axis segment [pos_mm-homo_region_mm , pos_mm+homo_region_mm]

    Possibility to add labels (= horizontal rules) on graph if dict_pos_mm_vs_label is specified.

    Parameters
    ----------
    df_field : pd.DataFrame
        Dataframe containing columns axis and Baxis
    axis: str
        Column name of the geometric axis to plot as x-axis (ex : 'y_mm')
    Baxis: str|list
        Column name(s) of the Baxis to plot as y-axis.
        Can be only one or a list of multiple Baxis to reprensent on the same graph (ex: 'By_total_mT' or ['By_coilA1_mT','By_coilA2_mT','By_total_mT'])
    is_zoom_on_pos : bool, optional
        If True, will plot between x-axis segment [pos_mm-homo_region_mm , pos_mm+homo_region_mm]. Otherwise will plot the full axis "axis". Default is False.
    pos_mm : float, optional
        Position in mm on "axis" on which the zoom should be centered. If specified but is_zoom_on_pos is False, it will still be used to display homogeneity value on subtitles if homo_region_mm is also defined.
    homo_region_mm : float, optional
    Baxis_homo : str, optional
        Specify which Baxis wanted for homogeneity calculation. If not specfied, will take last component of "total" in Baxis.
    dezoom_factor : float, optional
    dict_titles : dict[str|Any], optional
    dict_subtitles : dict[str|Any], optional
    dict_pos_mm_vs_label : dict, optional
        Dictionary containing the labels to display as pos_mm:"my_label"
        i.e : {'DUT position':12.5, 'Coil Left edge':6, 'Coil Right edge':19}
    is_save : bool, optional
        Default is False.
    save_filename : str, optional
    savepath_png : Path|str, optional
    savepath_html : Path|str, optional
    save_scale_factor : float, optional
        Magnification factor to have bigger (or smaller) graph as png/html files. Default is 1 (1:1)
    nb_plot_samples : int, optional
        Number of points plot on the Altair chart. If below the total number of point on the axis, it will take randomly distributed + ensuring the pos_mm is inside.
        Rationale : Altair supports max 5000 by default, and can be a bit laggy on Notebooks at max. Default culib is 4000.

    Returns
    -------
    chart : altair.Chart
        Chart as Altair Chart object

    Examples
    --------
    ## Create your coils + field

    >>> import culib as cul
    >>> df_field = cul.init_df_field()
    >>> coil_A = cul.RectangularCoil(
    ...    axis = 'z_mm',
    ...    X_in_mm = 42,
    ...    Y_in_mm = 82,
    ...    T_mm = 6,
    ...    L_mm = 20,
    ...    pos_mm = -30,
    ...    wire = cul.RoundWire(awg=22),
    ...    cur_A = 6.56)
    >>> df_field = coil_A.calc_field(df_field)
    >>> coil_B = cul.RectangularCoil(
    ...    axis = 'z_mm',
    ...    X_in_mm = 42,
    ...    Y_in_mm = 82,
    ...    T_mm = 6,
    ...    L_mm = 20,
    ...    pos_mm = +30,
    ...    wire = cul.RoundWire(awg=22),
    ...    cur_A = 6.56)
    >>> df_field = coil_B.calc_field(df_field)

    ## Plot 1 field vs 1 axis and save it as png and interactive html

    >>> savepath_png = './tests/data/output_plots/'
    >>> savepath_html = savepath_png + 'interactive_html/'
    >>> chart = cul.plot_field(
    ...     df_field, axis='z_mm', Baxis='Bz_total_mT',
    ...     is_save=True, savepath_png=savepath_png, savepath_html=savepath_html, save_filename='test_plot_field',
    ...     graphtitle="Main field along main axis of coil A + coil B",
    ...     dict_subtitles={'My param': 12, 'AWG':coil_A.wire.awg, 'Distance btw coils (mm)':coil_B.pos_mm - coil_A.pos_mm})

    ## Plot several fields on the same graph

    >>> chart = cul.plot_field(
    ...     df_field, axis='z_mm', Baxis=['Bz_coil_A_mT','Bz_coil_B_mT','Bz_total_mT'],
    ... )

    ## Plot with vertical labels on graph to display coil edges

    >>> dict_coil_edges = {
    ...     "A Left"  : coil_A.pos_mm - coil_A.L_mm/2 ,
    ...     "A Right" : coil_A.pos_mm + coil_A.L_mm/2 ,
    ...     "B Left"  : coil_B.pos_mm - coil_B.L_mm/2 ,
    ...     "B Right" : coil_B.pos_mm + coil_B.L_mm/2 ,
    ...  }
    >>> chart = cul.plot_field(
    ...     df_field, axis='z_mm', Baxis=['Bz_coil_A_mT','Bz_coil_B_mT','Bz_total_mT'],
    ...     dict_pos_mm_vs_label=dict_coil_edges,
    ...     is_save=True, savepath_png='./tests/data/output_plots/', save_filename='test_plot_field_labels',
    ... )

    ## Zoom on a segment and display homogeneity on graph

    >>> chart = cul.plot_field(
    ...     df_field, axis='z_mm', Baxis='Bz_total_mT',
    ...     is_zoom_on_pos=True, pos_mm = 0.0, homo_region_mm = 0.5,
    ...     dict_titles={'graphtitle':'MY BIG TITLE', 'Design version':1.2, 'Coucou':'Yes'}
    ... )

    ## Can specify savepaths as Path from pathlib (recommended)

    >>> from pathlib import Path
    >>> savepath_png = Path().cwd() / 'tests/data/output_plots'
    >>> chart = cul.plot_field(
    ...     df_field, axis='z_mm', Baxis='Bz_total_mT',
    ...     is_save=True, savepath_png=savepath_png, save_filename='test_plot_field',
    ... )

    ## 3D : Plot 3 fields components vs 1 axis from 3D df_field

    >>> df_field_3d = cul.init_df_field_3d(100, 2)
    >>> df_field_3d = coil_A.calc_field_3d(df_field_3d)
    >>> df_field_3d = coil_B.calc_field_3d(df_field_3d)
    >>> df_field_3d = cul.calc_total_fields(df_field_3d)
    >>> chart = cul.plot_field(
    ...     df_field_3d, axis='x_mm', Baxis=['Bx_total_mT', 'By_total_mT', 'Bz_total_mT'],
    ...     pos_mm = (0, 12, -4),
    ...     is_save=True, savepath_png=savepath_png, savepath_html=savepath_html, save_filename='test_plot_field_3D',
    ...     graphtitle="3D fields along main axis of coil A + coil_B",
    ...     dict_subtitles={'My param': 12, 'AWG':coil_A.wire.awg, 'Distance btw coils (mm)':coil_B.pos_mm - coil_A.pos_mm})

    ## 3D : ZOOM Plot 3 fields components vs 1 axis from 3D df_field

    >>> df_field_3d = cul.init_df_field_3d(100, 2)
    >>> df_field_3d = coil_A.calc_field_3d(df_field_3d)
    >>> df_field_3d = coil_B.calc_field_3d(df_field_3d)
    >>> df_field_3d = cul.calc_total_fields(df_field_3d)
    >>> chart = cul.plot_field(
    ...     df_field_3d, axis='x_mm', Baxis=['Bx_total_mT'],
    ...     is_zoom_on_pos = True, pos_mm = (6, 12, -4), homo_region_mm = 10,
    ...     is_save=True, savepath_png=savepath_png, savepath_html=savepath_html, save_filename='test_plot_field_3D_ZOOM',
    ...     graphtitle="3D fields along main axis of coil A + coil_B",
    ... )

    """

    # TODO (prio 2) idea for later for 3D : implement PlotAxis object ?

    log = get_local_logger("plot_field", **kwargs)

    # Validate arguments
    if is_zoom_on_pos:
        if pos_mm is None:
            pos_mm = DEFAULT_POS_MM
            err_msg = f"is_zoom_on_pos selected but pos_mm not defined. Set to default value (pos_mm={pos_mm}) "
            log.warning(err_msg)
        if homo_region_mm is None:
            homo_region_mm = DEFAULT_HOMO_REGION_MM
            err_msg = f"is_zoom_on_pos selected but homo_region_mm not defined. Set to default value (homo_region_mm={homo_region_mm}) "
            log.warning(err_msg)

    # Get df_plot from df_field
    df_plot = prepare_df_plot_field(
        df_field,
        axis,
        Baxis,
        is_zoom_on_pos=is_zoom_on_pos,
        pos_mm=pos_mm,
        homo_region_mm=homo_region_mm,
        dezoom_factor=dezoom_factor,
        nb_plot_samples=nb_plot_samples,
        **kwargs,
    )

    # Determine multiple Baxis or not
    if isinstance(Baxis, str):
        Baxis = [Baxis]
        log.debug("Baxis is a single str, transformed it as a list of 1 element")
    elif isinstance(Baxis, list):
        log.debug("Baxis specified is a list")
    else:
        err_msg = f"Baxis is neither a str nor a list, unknown type (Baxis={Baxis})"
        log.error(err_msg)
        raise TypeError(err_msg)

    # Get column name for B total or (if (one _) or total')
    if Baxis_homo is None:
        for B in reversed(Baxis):
            if ("total" in B) or (B.count("_") == 1):
                Baxis_homo = B
        if Baxis_homo is None:
            log.warning("did not find column representing total field for homogeneity calc (column should contain 'total' or only one '_')")  # fmt:skip
            Baxis_homo = Baxis[-1]
            log.warning(f"took last column of Baxis list as default : {Baxis_homo}")
        log.debug(f"B_field_column used for homo calc = {Baxis_homo}")

    # Calc homo ratio if applicable, in order to pass it to prepare_graphsubtitles()
    homo_percent = None
    if pos_mm is not None and homo_region_mm is not None:
        homo_percent = get_field_homo_at_pos(
            df_plot,
            axis=axis,
            Baxis=Baxis_homo,
            pos_mm=pos_mm,
            homo_region_mm=homo_region_mm,
        )
    else:
        log.debug("homo_percent not defined")

    # Get graph titles and subtitles
    list_graphtitles = prepare_graphtitles(
        axis=axis,
        is_zoom_on_pos=is_zoom_on_pos,
        pos_mm=pos_mm,
        homo_region_mm=homo_region_mm,
        dict_titles=dict_titles,
        **kwargs,
    )
    list_graphsubtitles = prepare_graphsubtitles(
        axis=axis,
        Baxis=Baxis,
        Baxis_column_homo=Baxis_homo,
        is_zoom_on_pos=is_zoom_on_pos,
        pos_mm=pos_mm,
        homo_region_mm=homo_region_mm,
        homo_percent=homo_percent,
        dict_subtitles=dict_subtitles,
        **kwargs,
    )

    # Create graph
    ## Fields graph
    chart_fields = generate_chart_fields(
        df_plot,
        axis,
        Baxis,
        list_graphtitles,
        list_graphsubtitles,
        dezoom_factor,
        **kwargs,
    )
    chart = chart_fields

    ## Labels graph
    if dict_pos_mm_vs_label:
        log.debug("adding labels to chart")
        chart_rules_and_labels = generate_chart_rules_and_labels(
            axis=axis,
            dict_pos_mm_vs_label=dict_pos_mm_vs_label,
            **kwargs,
        )
        chart += chart_rules_and_labels

    # Manage save
    if is_save:
        if save_filename is not None:
            save_chart(
                chart,
                save_filename,
                savepath_png=savepath_png,
                savepath_html=savepath_html,
                scale_factor=save_scale_factor,
                **kwargs,
            )
        else:
            log.error("issue with saving chart, is_save selected but save_filename not specified. Will skip saving.")  # fmt:skip

    return chart
