from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from scipy.special import ellipk, ellipe, elliprj

from culib.utils.logs import get_local_logger


def manage_cartesian_referential(
    coil_axis: str, x_ref: Any, y_ref: Any, z_ref: Any
) -> tuple[Any, Any, Any]:
    """
    Adapt cartesian coordinates system to convention used in the research article https://doi.org/10.1063/5.0010982
    (work from S. Hampton, R. A. Lane, R. M. Hedlof, R. E. Phillips and C. A. Ordonez)

    Returns permuted axes in correct order vs the actual coil axis.

    Parameters
    ----------
    coil_axis:str
        Name of the revolution axis of the coil. Must match with axis name in df_field (i.e: "x_mm", "y_mm" or "z_mm")
    x_ref
        Can be geom axis or field axis
    y_ref
        Can be geom axis or field axis
    z_ref
        Can be geom axis or field axis

    Returns
    -------
    x, y, z
        Tuple of permuted axes in correct order vs the actual coil axis
    """
    if coil_axis == "z_mm":
        x = x_ref
        y = y_ref
        z = z_ref
    elif coil_axis == "x_mm":
        x = z_ref
        y = y_ref
        z = x_ref
    elif coil_axis == "y_mm":
        x = x_ref
        y = z_ref
        z = y_ref
    else:
        err_msg = f"unknown axis (must be 'x_mm', 'y_mm' or 'z_mm'). Got {coil_axis}"
        raise ValueError(err_msg)
    return x, y, z


def Bfield_3d_rectangular_solenoid(
    df_field: pd.DataFrame,
    coil_axis: str,
    pos_x_mm: float,
    pos_y_mm: float,
    pos_z_mm: float,
    L_coil_mm: float,
    X_coil_mm: float,
    Y_coil_mm: float,
    n_turn: int,
    I_coil_A: float,
    is_delta_method: bool = False,
    delta_mm2: float = 1e-3,
) -> (pd.Series, pd.Series, pd.Series):
    """
    Calculate all 3 field components Bx=f(x,y,z), By=f(x,y,z) and Bz=f(x,y,z) for a finite rectangular solenoid along its revolution axis z.
    Take Position (x,y,z) from df_field.
    Finite Solenoid of Length L, single wire layer model (of mean X and Y)
    Integration of Biot-Savart law, as per https://doi.org/10.1063/5.0010982 (work from S. Hampton, R. A. Lane, R. M. Hedlof, R. E. Phillips and C. A. Ordonez)

    Parameters
    ----------
    df_field : pd.DataFrame
        Dataframe containing 'x_mm', 'y_mm' and 'z_mm' axis
    coil_axis : str
        Name of the revolution axis of the coil. Must match with axis name in df_field (i.e: "x_mm", "y_mm" or "z_mm")
    pos_x_mm : float
        Offset position in x in mm
    pos_y_mm : float
        Offset position in y in mm
    pos_z_mm : float
        Offset position in z in mm
    L_coil_mm: float
        Coil length, in mm
    X_coil_mm : float
        Coil width in X, in mm
    Y_coil_mm : float
        Coil width in Y, in mm
    n_turn : int
        Number of turn of wire
    I_coil_A : float
        Coil current in A
    is_delta_method : bool, optional
        If True, will add a small constant in expressions in order to avoid potential divergence of ratios in arctan. Default is False.
        To be used in case of issue.
    delta_mm2 : float, optional
        Value of delta in mm2. Must be "sufficiently small to have a negligible effect on calculation". Default is 1e-3.

    Returns
    -------
    Bx_mT : Series or Array
        Magnetic field on axis as Series or Array in mT
    By_mT : Series or Array
        Magnetic field on axis as Series or Array in mT
    Bz_mT : Series or Array
        Magnetic field on axis as Series or Array in mT
    """

    mu0 = 4 * np.pi * 1e-1  # in mT.mm/A
    B0_mT = mu0 * n_turn * I_coil_A / L_coil_mm  # in mT

    ax_mm = X_coil_mm / 2
    ay_mm = Y_coil_mm / 2
    az_mm = L_coil_mm / 2

    x_ref_mm = df_field["x_mm"] - pos_x_mm
    y_ref_mm = df_field["y_mm"] - pos_y_mm
    z_ref_mm = df_field["z_mm"] - pos_z_mm

    # Manage referential
    x_mm, y_mm, z_mm = manage_cartesian_referential(
        coil_axis, x_ref_mm, y_ref_mm, z_ref_mm
    )

    # Define radius modulation term (from formula, source link in docstring)
    def r(i, j, k):
        ri2 = (x_mm + ax_mm * (-1) ** (i + 1)) ** 2
        rj2 = (y_mm + ay_mm * (-1) ** (j + 1)) ** 2
        rk2 = (z_mm + az_mm * (-1) ** (k + 1)) ** 2
        r = np.sqrt(ri2 + rj2 + rk2)
        return r

    # Initialize summing terms, make sure they have same shape as z_mm series|array
    Bx_S1 = 0 * z_mm
    By_S1 = 0 * z_mm
    Bz_S1 = 0 * z_mm
    Bz_S2 = 0 * z_mm

    # Go for summing loops
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                rijk = r(i, j, k)
                Bx_sign = (-1) ** (i + j + k)
                By_sign = (-1) ** (i + j + k)
                Bz_sign = (-1) ** (i + j + k + 1)
                x_term = x_mm + ax_mm * (-1) ** (i + 1)
                y_term = y_mm + ay_mm * (-1) ** (j + 1)
                z_term = z_mm + az_mm * (-1) ** (k + 1)

                # Calc Bx term
                Bx_S1 += Bx_sign * np.log((-y_term + rijk) / (y_term + rijk))
                # Calc By term
                By_S1 += By_sign * np.log((-x_term + rijk) / (x_term + rijk))
                # Calc Bz term
                # fmt: off
                if is_delta_method:
                    delta_x_term = np.sqrt(delta_mm2+x_term**2)
                    delta_y_term = np.sqrt(delta_mm2+y_term**2)
                    Bz_S1 += Bz_sign * (y_term / delta_y_term) * np.arctan(x_term*z_term/(rijk*delta_y_term))
                    Bz_S2 += Bz_sign * (x_term / delta_x_term) * np.arctan(y_term*z_term/(rijk*delta_x_term))
                else:
                    Bz_S1 += Bz_sign * np.arctan(x_term * z_term / (y_term * rijk))
                    Bz_S2 += Bz_sign * np.arctan(y_term * z_term / (x_term * rijk))
                # fmt: on

    Bx_ref_mT = B0_mT / (8 * np.pi) * (Bx_S1)
    By_ref_mT = B0_mT / (8 * np.pi) * (By_S1)
    Bz_ref_mT = B0_mT / (4 * np.pi) * (Bz_S1 + Bz_S2)

    # Manage referential
    Bx_mT, By_mT, Bz_mT = manage_cartesian_referential(
        coil_axis, Bx_ref_mT, By_ref_mT, Bz_ref_mT
    )

    # TODO : Fix na/inf issues (fillna ?)

    return Bx_mT, By_mT, Bz_mT


def ellipp(n: float | pd.Series, m: float | pd.Series) -> float | pd.Series:
    """
    Legendre form of complete elliptic integral of the third kind.
    Uses implementation of 1st and 2nd kind from Scipy (Scipy has no implementation of 3rd kind...)

    From identities between Legendre's elliptic integrals as Symmetric elliptic integrals
    https://dlmf.nist.gov/19.25#i

    Notes
    -----
    Found at 1st sight a potential implementation (scipy github merge request), but is not OK (not matching)
    Tends to overestimate
    # y = 1 - m
    # rf = elliprf(0, y, 1)
    # rj = elliprj(0, y, 1, 1 - n)
    # p = rf + rj * n / 3

    """
    # n, m = (np.asarray(x) for x in (n, m))
    if np.any(m >= 1):
        m = m.where(m < 1)
        warn_msg = "got m values >= 1. Replaced corresponding lines with nan."
        log = get_local_logger("ellipp")
        log.warning(warn_msg)

    # Calc ellipk term (first kind)
    k = ellipk(m)

    # Calc elliprj term (second kind)
    ## Define the 4 arguments of elliprj
    rj_x1 = 0
    rj_x2 = 1 - m**2
    rj_x3 = 1
    rj_x4 = 1 - n

    ## Convert to np.ndarray (because might cause issues on some pandas versions)
    if isinstance(rj_x2, pd.Series):
        rj_x2 = rj_x2.values
    if isinstance(rj_x4, pd.Series):
        rj_x4 = rj_x4.values

    rj = elliprj(rj_x1, rj_x2, rj_x3, rj_x4)

    # Deduct ellipp from ellipk and elliprj
    p = k + rj * n / 3

    return p


def manage_val_around_zero(
    a: pd.Series, zero_prec: float, replace_with: float
) -> pd.Series:
    """
    Replace values around zero in an array with replace_with.
    Purpose of this func is to prevent division by 0 in calc functions

    Parameters
    ----------
    a : pd.Series
        Array/Series to look into
    zero_prec : float
        Absolute tolerance to consider a value to be close to zero. 1e-8 is OK good enough for float64.
    replace_with : float
        Value which will replace found values close to zero

    Returns
    -------
        Updated Series with values around zero replaced by replace_with value.
    """
    return a.mask(abs(a) < zero_prec, replace_with)


def Bfield_3d_circular_solenoid(
    df_field: pd.DataFrame,
    coil_axis: str,
    pos_x_mm: float,
    pos_y_mm: float,
    pos_z_mm: float,
    L_coil_mm: float,
    r_coil_mm: float,
    n_turn: int,
    I_coil_A: float,
    zero_prec_mT: float = 1e-4,
) -> (pd.Series, pd.Series, pd.Series):
    """
    Calculate all 3 field components Bx=f(x,y,z), By=f(x,y,z) and Bz=f(x,y,z) for a finite circular solenoid of revolution axis coil_axis.
    Take Position (x,y,z) from df_field.
    Finite Solenoid of Length L, single wire layer model (of mean radius R=(Rcoil_out+Rcoil_in)/2)
    Integration of Biot-Savart law, as per https://doi.org/10.1063/5.0010982 (work from S. Hampton, R. A. Lane, R. M. Hedlof, R. E. Phillips and C. A. Ordonez)

    Parameters
    ----------
    df_field : pd.DataFrame
        Dataframe containing 'x_mm', 'y_mm' and 'z_mm' axis
    coil_axis : str
        Name of the revolution axis of the coil. Must match with axis name in df_field (i.e: "x_mm", "y_mm" or "z_mm")
    pos_x_mm : float
        Offset position in x in mm
    pos_y_mm : float
        Offset position in y in mm
    pos_z_mm : float
        Offset position in z in mm
    L_coil_mm: float
        Coil length, in mm
    r_coil_mm : float
        Coil mean radius, in mm
    n_turn : int
        Number of turn of wire
    I_coil_A : float
        Coil current in A

    Returns
    -------
    Bx_mT : Series or Array
        Magnetic field on axis as Series or Array in mT
    By_mT : Series or Array
        Magnetic field on axis as Series or Array in mT
    Bz_mT : Series or Array
        Magnetic field on axis as Series or Array in mT
    """
    # Define const and var names
    mu0 = 4 * np.pi * 1e-1  # in mT.mm/A
    B0_mT = mu0 * n_turn * I_coil_A / L_coil_mm  # in mT

    a = r_coil_mm
    L = L_coil_mm

    # Define cartesian axis arrays from df_field
    x_ref_mm = df_field["x_mm"] - pos_x_mm
    y_ref_mm = df_field["y_mm"] - pos_y_mm
    z_ref_mm = df_field["z_mm"] - pos_z_mm

    x_mm, y_mm, z_mm = manage_cartesian_referential(
        coil_axis, x_ref_mm, y_ref_mm, z_ref_mm
    )

    # Convert cartesian pos to cylindrical pos
    ## Calc r from x,y and manage r=0
    r_mm = np.sqrt(x_mm**2 + y_mm**2)
    ### Replace 0 with a small value unsignificant value to avoid division by 0
    abs_zero_prec = 1e-8
    r_mm = manage_val_around_zero(r_mm, abs_zero_prec, abs_zero_prec)
    ## Calc theta from x,y and manage x=0
    theta_rad = np.arctan2(y_mm, x_mm)  # Case 0/0 will give 0 with np.arctan2 function

    # Define notations from paper
    ksi_p_mm = z_mm + L / 2
    ksi_m_mm = z_mm - L / 2

    u = 4 * a * r_mm / (a + r_mm) ** 2
    m_p = 4 * a * r_mm / ((a + r_mm) ** 2 + ksi_p_mm**2)
    m_m = 4 * a * r_mm / ((a + r_mm) ** 2 + ksi_m_mm**2)

    # Calc Br_mT
    Br_p = np.sqrt(a / (r_mm * m_p)) * (ellipe(m_p) - (1 - m_p / 2) * ellipk(m_p))
    Br_m = np.sqrt(a / (r_mm * m_m)) * (ellipe(m_m) - (1 - m_m / 2) * ellipk(m_m))

    Br_mT = B0_mT / np.pi * (Br_p - Br_m)

    # Calc Bz_mT
    Bz_p = (
        ksi_p_mm
        * np.sqrt(m_p / (a * r_mm))
        * (ellipk(m_p) + ((a - r_mm) / (a + r_mm)) * ellipp(u, m_p))
    )
    Bz_m = (
        ksi_m_mm
        * np.sqrt(m_m / (a * r_mm))
        * (ellipk(m_m) + ((a - r_mm) / (a + r_mm)) * ellipp(u, m_m))
    )

    Bz_mT = B0_mT / (4 * np.pi) * (Bz_p - Bz_m)

    # Convert cylindrical coordinates to cartesian ref (Br,Btheta to Bx,By)
    Bx_ref_mT = np.cos(theta_rad) * Br_mT  # as Btheta_mT = 0 by definition
    By_ref_mT = np.sin(theta_rad) * Br_mT  # as Btheta_mT = 0 by definition
    Bz_ref_mT = Bz_mT

    # Clean and manage around zero values (replace small values by zero)
    Bx_ref_mT = manage_val_around_zero(Bx_ref_mT, zero_prec_mT, 0)
    By_ref_mT = manage_val_around_zero(By_ref_mT, zero_prec_mT, 0)

    Bx_mT, By_mT, Bz_mT = manage_cartesian_referential(
        coil_axis, Bx_ref_mT, By_ref_mT, Bz_ref_mT
    )

    return Bx_mT, By_mT, Bz_mT
