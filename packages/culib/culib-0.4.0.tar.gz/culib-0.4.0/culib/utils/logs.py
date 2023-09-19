from __future__ import annotations

import logging

LOG_LEVEL_DEFAULT = logging.WARNING
LOG_FORMAT_DEFAULT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
LOG_DATEFORMAT_DEFAULT = "%d/%m/%Y %H:%M:%S"


def init_culib_logging(
    log_level: str | int = LOG_LEVEL_DEFAULT, force: bool = True
) -> None:
    """
    Initialize loggings from all culib by calling logging.basicConfig().
    To be called after import if wanting to display logs of the lib.

    Parameters
    ----------
    log_level:str|int
        Log level required as str compliant with logging lib (i.e: "INFO", "DEBUG", "ERROR"...) or int (i.e : 10, 40...)
    force:bool, optional
         Force logging to use culib log format and default level, as it calls logging.basicConfig (which can be ran only "once"). Default is True

    Examples
    --------
    >>> import culib as cul
    >>> cul.init_culib_logging("INFO")

    """

    # Set default settings of rootlogger
    logging.basicConfig(
        format=LOG_FORMAT_DEFAULT,
        datefmt=LOG_DATEFORMAT_DEFAULT,
        level=log_level,
        force=force,
    )


def get_local_logger(name: str, **kwargs) -> logging.Logger:
    """
    Create a dedicated logger, allowing to display a custom name of location in the log messages
    If log_level in arguments, it will reflect it on the local logger to set at required log level.
    Else it will use current log level of root logger.

    Parameters
    ----------
    name:str
        Logger name

    Returns
    -------
    logger:logging.Logger
        Local logger

    Examples
    >>> logger = get_local_logger('my_function')
    >>> logger.warning('This is a local warning from blabla')

    >>> logger = get_local_logger('my_object_to_debug', log_level='DEBUG')
    """

    logger = logging.getLogger(name)
    if "log_level" in kwargs.keys() and kwargs["log_level"] is not None:
        log_level = kwargs["log_level"]
    else:
        log_level = logging.root.getEffectiveLevel()
    logger.setLevel(log_level)
    return logger
