"""Various spheroid parameters
Author: C. Grima (cyril.grima@gmail.com)
"""

import scipy.constants as ct
from numpy import pi, log, sqrt, sin, cos, arccos
from scipy.special import ellipkinc, ellipeinc
import numpy as np


def area(a, c=0):
	"""Area of a spheroid
	a = equatorial radius
	c = polar radius
	"""
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


def density(mass, a, c=0):
	"""Mass of a spheroid
	a = equatorial radius
	c = polar radius (default=0)
	"""
	return mass/volume(a, c)


def ellipticity(a, c):
	"""Spheroid eccentricity
	a = equatorial radius
	c = polar radius
	"""
	if a > c:  # oblate
		output = sqrt(1-c**2/a**2)
	elif a < c:  # prolate
		output = sqrt(1-a**2/c**2)
	else:
		output = 0.
	return output


def flattening(a, c):
	"""Flattening of a spheroid
	a = equatorial radius
	c = polar radius
	"""
	return (a-c)/a


def gravity(radius, mass):
	"""Gravity
	"""
	return ct.G*mass/radius**2


def radius_volumic(volume):
	"""Volumic radius
	"""
	return (3.*volume/4/pi)**(1/3.)


def volume(a, c=0):
	"""Volume of a spheroid
	a = equatorial radius
	c = polar radius (default=0)
	"""
	if c and c != a:
		output = (4./3)*pi*a**2*c
	else:
		output = (4./3)*pi*a**3
	return output

