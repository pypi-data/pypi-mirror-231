from __future__ import annotations

from culib.utils.logs import get_local_logger
from culib.wires.data_wires import *
from culib.wires.basewire import (
    Wire,
    DEFAULT_MATERIAL,
    DEFAULT_T_INSULATION_MM,
    DEFAULT_TEMP_DEGC,
)


class FoilWire(Wire):
    """
    Class definition for Foil Wire objects.
    Simply subclass of Wire object, with shape=FOIL passed at init + protection to not change shape property

    Needed parameters
    -----------------
    L_foil_mm : float, optional
        Length of the foil wire, in mm.
    t_foil_mm : float, optional
        Thickness of the foil wire, in mm.
    """

    def __init__(
        self,
        material: str = DEFAULT_MATERIAL,
        temp_degC: float = DEFAULT_TEMP_DEGC,
        t_insulation_mm: float = DEFAULT_T_INSULATION_MM,
        L_foil_mm: float = None,
        t_foil_mm: float = None,
        is_autorecalc: bool = True,
        **kwargs,
    ):
        super().__init__(
            shape=FOIL,
            material=material,
            temp_degC=temp_degC,
            t_insulation_mm=t_insulation_mm,
            L_foil_mm=L_foil_mm,
            t_foil_mm=t_foil_mm,
            is_autorecalc=is_autorecalc,
            logger=get_local_logger("FoilWire", **kwargs),
            **kwargs,
        )

        delattr(self, "r_curv_squarecorner_mm")

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        err_msg = "cannot modify shape of FoilWire object. Use general Wire object or RoundWire or SquareWire to have a wire with a different shape."
        self.log.error(err_msg)
        raise AttributeError(err_msg)

    def _validate_r_curv_squarecorner_mm(self, r_curv_squarecorner_mm, force=False):
        pass
