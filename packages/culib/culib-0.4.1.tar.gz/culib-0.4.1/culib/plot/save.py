from __future__ import annotations

from pathlib import Path

import vl_convert as vlc

from culib.utils.logs import get_local_logger


def save_chart_as_html(
    chart, filename: str, savepath: Path | str, scale_factor=1.0, **kwargs
):
    """
    ex:
    """
    log = get_local_logger("save_chart_as_html", **kwargs)

    if isinstance(savepath, Path):
        savefilepath = (savepath / filename).with_suffix(".html")
    elif isinstance(savepath, str):
        filename = filename.split(".html")[0]
        savefilepath = f"{savepath}/{filename}.html"
        savefilepath = savefilepath.replace("//", "/")
    else:
        err_msg = (
            f"savepath is neither a string nor a pathlib.Path, savepath={savepath}"
        )
        log.error(err_msg)
        raise TypeError(err_msg)
    chart.save(savefilepath, scale_factor=scale_factor)
    log.info(f"successfully saved as .html version in {savefilepath}")


def save_chart_as_png(
    chart, filename: str, savepath: Path | str, scale_factor=1.0, **kwargs
):
    """
    ex:
    """
    log = get_local_logger("save_chart_as_png", **kwargs)

    if isinstance(savepath, Path):
        savefilepath = (savepath / filename).with_suffix(".png")
    elif isinstance(savepath, str):
        filename = filename.split(".png")[0]
        savefilepath = f"{savepath}/{filename}.png"
        savefilepath = savefilepath.replace("//", "/")
    else:
        err_msg = f"savepath is not a string nor a pathlib.Path, savepath={savepath}"
        log.error(err_msg)
        raise TypeError(err_msg)

    try:
        chart.save(savefilepath, scale_factor=scale_factor)
    except (ModuleNotFoundError, ImportError):
        log.warning("have to deal with old Altair version (< 5.0), will save as .png differently")  # fmt:skip
        png_data = vlc.vegalite_to_png(chart.to_dict(), scale=scale_factor)
        with open(savefilepath, "wb") as f:
            f.write(png_data)

    log.info(f"successfully saved as .png version in {savefilepath}")


def save_chart(
    chart,
    filename: str,
    savepath_png: Path | str = None,
    savepath_html: Path | str = None,
    scale_factor: float = 1.0,
    **kwargs,
):
    log = get_local_logger("save_chart", **kwargs)
    # Check
    if savepath_png is None and savepath_html is None:
        err_msg = "no savepath specified for both png and html"
        log.error(err_msg)
        raise ValueError(err_msg)
    # Save as html
    if savepath_html is not None:
        save_chart_as_html(
            chart, filename, savepath_html, scale_factor=scale_factor, **kwargs
        )
    # Save as png
    if savepath_png is not None:
        save_chart_as_png(
            chart, filename, savepath_png, scale_factor=scale_factor, **kwargs
        )
