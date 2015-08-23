"""Various spheroid parameters
Author: C. Grima (cyril.grima@gmail.com)
"""

import scipy.constants as ct
from numpy import pi, log, sqrt, sin, cos, arccos
from scipy.special import ellipkinc, ellipeinc
import numpy as np


def area(rad):
    """Area of a spheroid

    Arguments
    ---------
    rad : dict
        {'a', 'b', 'c'} Equatorial1, Equatorial2, and polar radius
    """
    a, b, c = rad['a'], rad['b'], rad['c']
    if c and c != a:  # spheroid
        b = a
        e = ellipticity(a, c)
        if a > c:  # oblate
            phi = arccos(c/a)
            m = (a**2 * (b**2 - c**2)) / (b**2 * (a**2 - c**2))
            tmp = ellipeinc(phi, m)*sin(phi)**2 + ellipkinc(phi, m)*cos(phi)**2
            output = 2*pi*(c**2 + a*b*tmp/sin(phi))
        elif a < c:  # prolate
            output = 0.
    else:  #sphere
        output = 4*pi*a**2
    return output


def density(mass, rad):
    """Mass of a spheroid

       Arguments
    ---------
    rad : dict
        {'a', 'b', 'c'} Equatorial1, Equatorial2, and polar radius
    """
    a, b, c = rad['a'], rad['b'], rad['c']
    return mass/volume(a, c)


def ellipticity(rad):
    """Spheroid eccentricity

    Arguments
    ---------
    rad : dict
        {'a', 'b', 'c'} Equatorial1, Equatorial2, and polar radius
    """
    a, b, c = rad['a'], rad['b'], rad['c']
    if a > c:  # oblate
        output = sqrt(1-c**2/a**2)
    elif a < c:  # prolate
        output = sqrt(1-a**2/c**2)
    else:
        output = 0.
    return output


def flattening(rad):
    """Flattening of a spheroid

    Arguments
    ---------
    rad : dict
        {'a', 'b', 'c'} Equatorial1, Equatorial2, and polar radius
    """
    a, b, c = rad['a'], rad['b'], rad['c']
    return (a-c)/a


def gravity(radius, mass):
    """Gravity

    Arguments
    ---------
	radius : float
        mean radius
	mass : float
        body mass
    """
    return ct.G*mass/radius**2


def lonlat2rad(lon, lat, rad):
    """Give the radius to a lon/lat coordinate

    Arguments
    ---------
    lon : float
        longitude
    lat : float
        latitude
    rad : dict
        {'a', 'b', 'c'} Equatorial1, Equatorial2, and polar radius
    """
    x, y, z = lonlat2xyz(lon, lat, rad)
    return sqrt(x**2 + y**2 + z**2)


def lonlat2xyz(lon, lat, rad):
    """Give the x, y, z coordinates from spherical coordinates

    Arguments
    ---------
    lon : float
        longitude
    lat : float
        latitude
    rad : dict
        {'a', 'b', 'c'} Equatorial1, Equatorial2, and polar radius
    """
    u, v = lat*pi/180., lon*pi/180.
    x = rad['a']*cos(u)*cos(v)
    y = rad['b']*cos(u)*sin(v)
    z = rad['c']*sin(u)
    return x, y, z


def radius_volumic(volume):
    """Volumic radius

    Arguments
    ---------
    volume : string
        body volume
	"""
    return (3.*volume/4/pi)**(1/3.)


def volume(rad):
    """Volume of a spheroid

    Arguments
    ---------
    rad : dict
        {'a', 'b', 'c'} Equatorial1, Equatorial2, and polar radius
    """
    a, b, c = rad['a'], rad['b'], rad['c']
    if c and c != a:
        output = (4./3)*pi*a**2*c
    else:
        output = (4./3)*pi*a**3
    return output

