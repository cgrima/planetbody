"""Various properties from Jupiter's moon Europa
Author: C. Grima (cyril.grima@gmail.com)
"""

import exosphere
from planetbody.Classdef import Body


nfo = Body('moon',  # category
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
           -1,  # longitude of the periapsis argument [deg]
           -1  # Ascending node [deg]
          )
