"""
Various exospheric properties for Jupiter's moon Europa 
Author: C. Grima (cyril.grima@gmail.com)
"""

import numpy as np
from scipy import interpolate


def o2_z(h, source='cassidy2007', kind='cubic'):
  """Neutral O2 density profile at Europa [m**-3]	
  h = vertical scale [m]
  """

  if source == 'cassidy2007':
    """From Cassidy et al. [2007]
    """
    z = np.array([0., 105, 200, 300, 400, 600, 800, 1000, 1200])*1e3
    n = np.log10(np.array([5e8, 3.5e6, 1.2e5, 3.3e4, 2e4, 1.3e4, 8.5e3, 6e3,
                           4e3]))
    f = interpolate.interp1d(z, n, kind=kind)

  return 10**f(h)*1e6


def electron_z(h, source='kliore1997', profil=3, kind='cubic'):
	"""Electron density profile at Europa [m**-3]
	h = vertical scale [m]
	kind = interpolation technique
	"""

	if source == 'kliore1997':
		"""From Kliore et al. [1997]
		profil 1, 2, and 3 = low, medium, high activity ionosphere
		"""
		z = np.array([0., 100, 200, 300, 400, 500,
                      600, 700, 800, 900, 1000])*1e3
		ne = np.array([[5e9, 3e9, 1.9e9, 1.2e9, .9e9, .75e9, #profil 1
    	                .6e9, .45e9, .3e9, .23e9, .2e9],
    	               [8.9e9, 6e9, 3.7e9, 2.6e9, 2e9, 1.55e9, #profil 2
    	                1.2e9, .95e9, .75e9, .63e9, .55e9],
    	               [13.5e9, 9.1e9, 6.3e9, 4.45e9, 3.5e9, 2.9e9, #profil 3
    	                2.4e9, 2e9, 1.65e9, 1.35e9, 1.1e9]])
		nonan = np.isnan(ne[profil-1,:])
		f = interpolate.interp1d(z[nonan == False], ne[profil-1, nonan == False],
                                 kind=kind)

	return f(h)
