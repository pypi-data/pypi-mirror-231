from __future__ import annotations

import numpy as np
import pandas as pd


def Bfield_axis_circular_solenoid(
    x_mm: np.ndarray | pd.Series,
    L_coil_mm: float,
    r_coil_mm: float,
    n_turn: int,
    I_coil_A: float,
    **kwargs,
) -> np.ndarray | pd.Series:
    """
    Calculate Bx=f(x) field value of a finite solenoid along its revolution axis x
    Finite Solenoid of Length L, single wire layer model (of mean radius R=(Rcoil_out+Rcoil_in)/2)
    Integration of Biot-Savart law

    Parameters
    ----------
    x_mm : Series or Array
        axis as Series or Array, in mm
    L_coil_mm : float
        Coil length in mm
    r_coil_mm : float
        Coil mean radius in mm
    n_turn : int
        Number of turn of wire
    I_coil_A : float
        Coil current in A

    Returns
    -------
    Bfield_mT : Series or Array
        Magnetic field on axis as Series or Array in mT
    """
    # log = get_local_logger('Bfield_axis_circular_solenoid', **kwargs)
    # fmt: off
    mu0 = 4*np.pi*1e-1 #in mT.mm/A
    B0_mT = mu0*n_turn*I_coil_A/(2*L_coil_mm) #in mT
    S1 = (L_coil_mm/2+x_mm)/(np.sqrt(r_coil_mm**2+(L_coil_mm/2+x_mm)**2))
    S2 = (L_coil_mm/2-x_mm)/(np.sqrt(r_coil_mm**2+(L_coil_mm/2-x_mm)**2))
    Bx_mT = B0_mT*( S1 + S2 )
    # fmt: on

    return Bx_mT


def Bfield_axis_rectangular_solenoid(
    z_mm: np.ndarray | pd.Series,
    L_coil_mm: float,
    X_coil_mm: float,
    Y_coil_mm: float,
    n_turn: int,
    I_coil_A: float,
    is_delta_method: bool = False,
    delta_mm2: float = 1e-3,
    **kwargs,
) -> np.ndarray | pd.Series:
    """
    Calculate Bz=f(z) for x=0,y=0 field value of a finite rectangular solenoid along its revolution axis z
    Finite Solenoid of Length L, single wire layer model (of mean X and Y)
    Integration of Biot-Savart law, as per https://doi.org/10.1063/5.0010982 (work from S. Hampton, R. A. Lane, R. M. Hedlof, R. E. Phillips and C. A. Ordonez)

    Parameters
    ----------
    z_mm : Series or Array
        axis as Series or Array, in mm
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
    delta_mm2 : float, optional
        Value of delta in mm2. Must be "sufficiently small to have a negligible effect on calculation". Default is 1e-3.

    Returns
    -------
    Bz_mT : Series or Array
        Magnetic field on axis as Series or Array in mT
    """
    # log = get_local_logger('Bfield_axis_rectangular_solenoid', **kwargs)

    k = 1e-1  # in mT.mm/A
    B0_mT = k * n_turn * I_coil_A / L_coil_mm  # in mT

    ax = X_coil_mm / 2
    ay = Y_coil_mm / 2
    az = L_coil_mm / 2

    S1 = 0 * z_mm  # To be sure to have same shape as z_mm series|array
    S2 = 0 * z_mm

    def r(i, j, k):
        r = np.sqrt( ax**2 + ay**2 + (z_mm + az*(-1)**(k+1))**2 )  # fmt: skip
        return r

    # fmt: off
    # Go for summing loops
    for i in (0,1):
        for j in (0,1):
            for k in (0,1):
                rijk = r(i,j,k)
                if is_delta_method:
                    S1 += (-1)**(i+j+k+1) * ((ay*(-1)**(j+1)) / (np.sqrt(delta_mm2+ay**2))) * np.arctan( (ax*(-1)**(i+1)*(z_mm + az*(-1)**(k+1))) / (rijk*np.sqrt(delta_mm2+ay**2)) ) #fmt: skip
                    S2 += (-1)**(i+j+k+1) * ((ax*(-1)**(i+1)) / (np.sqrt(delta_mm2+ax**2))) * np.arctan( (ay*(-1)**(j+1)*(z_mm + az*(-1)**(k+1))) / (rijk*np.sqrt(delta_mm2+ax**2)) ) #fmt: skip
                else:
                    S1 += (-1)**(i+j+k+1) * np.arctan( ((-1)**(i-j)*ax*(z_mm+az*(-1)**(k+1))) / (ay*rijk) ) #fmt: skip
                    S2 += (-1)**(i+j+k+1) * np.arctan( ((-1)**(j-i)*ay*(z_mm+az*(-1)**(k+1))) / (ax*rijk) ) #fmt: skip
    # fmt: on

    Bz_mT = B0_mT * (S1 + S2)

    return Bz_mT
