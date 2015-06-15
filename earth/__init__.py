"""Various properties from Earth
Author: C. Grima (cyril.grima@gmail.com)
"""

from planetbody.Classdef import Body

nfo = Body('planet',  # category
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
