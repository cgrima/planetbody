"""Various python classes planetary usage
Author: C. Grima (cyril.grima@gmail.com)
"""

from planetbody import ellipsoid
from planetbody import orbit


class Body:
    """Planet class (name, adjective, acronym, parent)
    in respect with the ecliptic (Earth)
    """
    def __init__(self, category, name, adjective, acronym, parent, mass, radius,
                 rotation, semimaj, apoapsis, periapsis,
                 axtilt, inclination, periarg, ascnode):
        self.category = category
        self.name = name
        self.adjective = adjective
        self.acronym = acronym
        self.parent = parent  # parent body
        self.mass = {'val':mass, 'unit':'kg'}  # mass
        self.radius = {'val':radius, 'unit':'m'}  # equatorial radius {a, b, c}
        self.rotation = {'val':rotation, 'unit':'days'}  # rotation [days]
        self.semimaj = {'val':semimaj, 'unit':'m'}  # semimajor axis
        self.apoapsis = {'val':apoapsis, 'unit':'m'}  # apoapsis radius
        self.periapsis = {'val':periapsis, 'unit':'m'}  # periaspsis radius
        self.axtilt = {'val':axtilt, 'unit':'deg'}  # rotation axis tilt
        self.inclination = {'val':inclination, 'unit':'deg'}  # orbit plan inclination
        self.periarg = {'val':periarg, 'unit':'deg'}  # longitude of the periapsis argument
        self.ascnode = {'val':ascnode, 'unit':'deg'}  # Ascending node

    def area(self):
        val = ellispoid.area(self.radius['val']['a'],
                             self.radius['val']['c'])
        return {'val':val, 'unit':'m^2'}

    def density(self):
        val = ellipsoid.density(self.mass['val'],
                                self.radius['val']['a'],
                                self.radius['val']['c'])
        return {'val':val, 'unit':'kg.m^{-3}'}

    def ellipticity(self):
        val = ellipsoid.ellipticity(self.radius['val']['a'],
                                    self.radius['val']['c'])
        return {'val':val, 'unit':None}

    def flattening(self):
        val = ellipsoid.flattening(self.radius['val']['a'],
                                   self.radius['val']['c'])
        return {'val':val, 'unit':None}

    def volume(self):
        val = ellipsoid.volume(self.radius['val']['a'],
                               self.radius['val']['c'])
        return {'val':val, 'unit':'m^{-3}'}

    def radius_mean(self):
        val = ellipsoid.radius_volumic(self.volume()['val'])
        return {'val':val, 'unit':'m'}

    def gravity_mean(self):
        val = ellispoid.gravity(self.radius_mean()['val'], self.mass['val'])
        return {'val':val, 'unit':'m.s^{-2}'}

