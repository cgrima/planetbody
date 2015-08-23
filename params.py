"""
Fundamenta parameters for planetary bodies
Author: C. Grima (cyril.grima@gmail.com)
"""

from planetbody.Classdef import Body
from planetbody import europa_func
import numpy as np


earth = Body('planet',  # category
             'Earth',  # name
             'terrestrial',  # adjective
             'S III',  # acronym
             'Sun',  # parent body
             5.97219e24,  # mass [kg]
             {'a':6378.137e3,
              'b':6378.137e3,
              'c':6356.752e3}, # radius [m]
             0.99726968,  # rotation [days]
             149598261e3,  # semimajor axis [m]
             15193000e3,  # apoapsis radius [m]
             147095000e3,  # periaspsis radius [m]
             26.4373,  # rotation axis tilt [deg]
             0.00005,  # orbit plan inclination [deg]
             102.94719,  # longitude of the periapsis argument [deg]
             -11.26064  # Ascending node [deg]
            )


europa = Body('moon',  # category
              'Europa',  # name
              'Europan',  # adjective
              'J II',  # acronym
              'Jupiter',  # parent body
              4.7998e22,  # mass [kg]
              {'a':1560.8e3,
               'b':1560.8e3,
               'c':1560.8e3}, # radius [m]
              3.551181041,  # rotation [days]
              671100e3,  # semimajor axis [m]
              677408e3,  # apoapsis radius [m]
              664792e3,  # periaspsis radius [m]
              0.1,  # rotation axis tilt [deg]
              0.466,  # orbit plan inclination [deg]
              np.nan,  # longitude of the periapsis argument [deg]
              np.nan  # Ascending node [deg]
             )
europa.exosphere = europa_func.exosphere


mars = Body('planet',  # category
            'Mars',  # name
            'Martian',  # adjective
            'S IV',  # acronym
            'Sun',  # parent body
            6.4185e23,  # mass [kg]
            {'a':3396.2e3,
             'b':3396.2e3,
             'c':3376.2e3}, # radius [m]
            1.025957,  # rotation [days]
            227939100e3,  # semimajor axis [m]
            249200000e3,  # apoapsis radius [m]
            206700000e3,  # periaspsis radius [m]
            25.19,  # rotation axis tilt [deg]
            1.850,  # orbit plan inclination [deg]
            286.537,  # longitude of the periapsis argument [deg]
            49.562  # Ascending node [deg]
           )
