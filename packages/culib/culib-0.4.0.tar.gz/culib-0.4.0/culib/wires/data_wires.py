from __future__ import annotations

import numpy as np

# Define shapes

ROUND = "round"
SQUARE = "square"
FOIL = "foil"

LIST_WIRE_SHAPES = [ROUND, SQUARE, FOIL]

# Define materials

COPPER = "copper"
ALUMINUM = "aluminum"

LIST_WIRE_MATERIALS = [COPPER, ALUMINUM]

# TODO (prio 2) : document source of data for material constants
DICT_TEMP_COEF_RESISTIVITY_PERDEGC_VS_MATERIAL = {
    COPPER: 4.04e-3,
    ALUMINUM: 3.90e-3,
}

DICT_RHO_RESISTIVITY_METEROHM_VS_MATERIAL = {
    COPPER: 1.68e-8,  # Data from wiki a bit overestimated (might apply 0.88*)
    ALUMINUM: 2.65e-8,
}

# TODO (prio 3) : take avg insulation in account
DICT_MASS_DENSITY_GPERCM3_VS_MATERIAL = {
    COPPER: 8.96,
    ALUMINUM: 2.70,
}

# Define AWG wire data ([Wikipedia AWG table](https://en.wikipedia.org/wiki/American_wire_gauge))
DICT_D_WIRE_IN_MM_VS_AWG = {
    0: 8.251,
    1: 7.348,
    2: 6.544,
    3: 5.827,
    4: 5.189,
    5: 4.621,
    6: 4.115,
    7: 3.665,
    8: 3.264,
    9: 2.906,
    10: 2.588,
    11: 2.305,
    12: 2.053,
    13: 1.828,
    14: 1.628,
    15: 1.450,
    16: 1.291,
    17: 1.150,
    18: 1.024,
    19: 0.912,
    20: 0.812,
    21: 0.723,
    22: 0.644,
    23: 0.573,
    24: 0.511,
    25: 0.455,
    26: 0.405,
    27: 0.361,
    28: 0.321,
    29: 0.286,
    30: 0.255,
    31: 0.227,
    32: 0.202,
    33: 0.180,
    34: 0.160,
    35: 0.143,
    36: 0.127,
}


# Define functions
def get_recommended_insulation_thickness(d_in_mm: float) -> float:
    """
    Get recommended insulation thickness from IEC 60317 and AWG NEMA MW1000C norms for the maximum grade 3 insulation.
    Took the max values to get maximum safety margins.
    Reverse engineered relationship from data tables available here : https://www.elektrisola.com/en/Products/Enamelled-Wire/Technical-Data

    Parameters
    ----------
    d_in_mm : float
        Wire inner diameter (without insulation...) in mm

    Returns
    -------
    t_insulation_mm : float
        Recommended insulation thickness in mm

    Examples
    --------
    # Get recommended ins. thickness for AWG 24 (which should corresponds to ~0.05mm)

    >>> get_recommended_insulation_thickness(0.511)
    0.04007228622443135

    Notes
    -----
    Polynomial gives shit when extrapolated... hence the ln function, which also corresponds a bit better to physics reality....
    #-0.1269*d_in_mm**2 + 0.1471*d_in_mm + 0.003
    """

    t_insulation_mm = 0.02 * np.log(d_in_mm) + 0.0535
    return t_insulation_mm
