# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import math


def get_fixed_diameter(dT_set, max_demand, dp_set):
    # based on UESgraphs Utilities size hydraunic network

    # fixed Diameter Values
    diameters = [
        0.015,
        0.02,
        0.025,
        0.032,
        0.04,
        0.05,
        0.065,
        0.08,
        0.1,
        0.125,
        0.15,
        0.2,
        0.25,
        0.3,
        0.35,
        0.4,
        0.45,
        0.5,
        0.6,
        0.7,
        0.8,
        0.9,
        1.0,
        1.1,
        1.2,
    ]

    # calculate m_flow
    cp = 4180  # J/(kg*K)
    m_flow = max_demand / (cp * dT_set)

    # increase Diameter until set pressure drop is reached or exceeded
    dp_spec = 1e99  # Pa/m
    i = 0
    diameter = diameters[i]
    while dp_spec > dp_set:
        diameter = diameters[i]
        darcy_friction_factor = 0.025   # Rohrreibungszahl
        water_density = 983
        dp_spec = 8 * darcy_friction_factor / (diameter ** 5 * math.pi ** 2 * water_density) * m_flow ** 2
        i += 1

    return diameter


def get_optimal_diameter(dT_set, max_demand, dp_set):
    # based on UESgraphs Utilities size hydraunic network

    # calculate m_flow
    cp = 4180  # J/(kg*K)
    m_flow = max_demand / (cp * dT_set)

    # constants
    darcy_friction_factor = 0.025  # Rohrreibungszahl
    water_density = 983
    diameter = (8*darcy_friction_factor*m_flow**2/(
            water_density*math.pi**2*dp_set))**(1/5)

    return diameter


def get_max_allowed_flow_velocity(dn, is_supply_pipe=True):

    # from Nussbaumer: http://dx.doi.org/10.1016/j.energy.2016.02.062.
    diameters = {
        0.015: [0.6, 0.5],
        0.02: [0.6, 0.5],
        0.025: [1.0, 0.6],
        0.032: [1.1, 0.8],
        0.04: [1.2, 1.0],
        0.05: [1.4, None],
        0.065: [1.6, None],
        0.08: [1.8, None],
        0.1: [1.9, None],
        0.125: [2.0, None],
        0.15: [2.5, None],
        0.2: [3.3, None],
        0.25: [3.9, None],
        0.3: [4.3, None],
        0.35: [4.6, None],
        0.4: [5.0, None],
        0.45: [None, None],
        0.5: [None, None],
        0.6: [None, None],
        0.7: [None, None],
        0.8: [None, None],
        0.9: [None, None],
        1.0: [None, None],
        1.1: [None, None],
        1.2: [None, None]
    }
    diameters_df = pd.DataFrame(data=diameters)
    diameters_df = diameters_df.transpose()
    diameters_df.rename(columns={0: "max flow supply pipe",
                                 1: "max flow connecting pipe"},
                        inplace=True)

    # decide if connecting or supply pipe. conencting pipes are the ones
    # directly conencted to houses and thus smaller max. allowed flow
    # velocities due to noise emissions
    if is_supply_pipe:
        col = "max flow supply pipe"
    else:
        col = "max flow connecting pipe"

    velocity = diameters_df.loc[dn, col]

    return velocity  # in m/s


def get_flow_velocity(diameter, max_demand, dT):

    cp = 4180  # J/(kg*K)
    m_flow = max_demand / (cp * dT)

    # water_density = 983     # at 60°C
    water_density = 999     # at 0-20°C

    velocity = m_flow / (water_density * math.pi * diameter**2)

    return velocity
