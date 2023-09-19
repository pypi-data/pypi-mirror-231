"""
Coils Utilities Library (CULib) is a Python package for modeling air-core electromagnet coils and calculating their physical characteristics based on their geometry and wire informations.

It also includes functions for calculating and plotting static magnetic field in 3D.

Please refer to https://gitlab.melexis.com/ple/culib for more infos / docs.
"""

__version__ = "0.4.0"

__all__ = [
    "init_culib_logging",
    "init_df_field",
    "init_df_field_3d",
    "calc_total_fields",
    "get_field_at_pos",
    "get_field_homo_at_pos",
    "rescale_current_for_field",
    "CircularCoil",
    "RectangularCoil",
    "plot_field",
    "Wire",
    "RoundWire",
    "SquareWire",
    "FoilWire",
]

# Import everything that can be seen as culib.xxx when user imports culib
from culib.utils.logs import init_culib_logging

from culib.field.df_field import init_df_field, init_df_field_3d, calc_total_fields
from culib.field.getters import (
    get_field_at_pos,
    get_field_homo_at_pos,
    rescale_current_for_field,
)

from culib.coils.circularcoil import CircularCoil
from culib.coils.rectangularcoil import RectangularCoil

from culib.plot.plot_field import plot_field

from culib.wires.basewire import Wire
from culib.wires.roundwire import RoundWire
from culib.wires.squarewire import SquareWire
from culib.wires.foilwire import FoilWire
