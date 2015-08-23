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
        val = ellipsoid.area(self.radius['val'])
        return {'val':val, 'unit':'m^2'}

    def density(self):
        val = ellipsoid.density(self.mass['val'],
                                self.radius['val'])
        return {'val':val, 'unit':'kg.m^{-3}'}

    def ellipticity(self):
        val = ellipsoid.ellipticity(self.radius['val'])
        return {'val':val, 'unit':None}

    def flattening(self):
        val = ellipsoid.flattening(self.radius['val'])
        return {'val':val, 'unit':None}

    def volume(self):
        val = ellipsoid.volume(self.radius['val'])
        return {'val':val, 'unit':'m^{-3}'}

    def radius_mean(self):
        val = ellipsoid.radius_volumic(self.volume()['val'])
        return {'val':val, 'unit':'m'}

    def gravity_mean(self):
        val = ellipsoid.gravity(self.radius_mean()['val'], self.mass['val'])
        return {'val':val, 'unit':'m.s^{-2}'}

    def report(self):
        buff = []
        add = buff.append
        add(self.name+' ('+self.acronym+') is a '+self.category+
            ' orbiting '+self.parent+'\n')
        add('\n')
        add('\t[Physical Properties]\n')
        add('\tMass           = %.2e %s\n' % (self.mass['val'],
                                              self.mass['unit']))
        add('\tRadius (Mean)  = %.2e %s\n' % (self.radius_mean()['val'],
                                              self.radius_mean()['unit']))
        add('\tRadius (Equ.1) = %.2e %s\n' % (self.radius['val']['a'],
                                              self.radius['unit']))
        add('\tRadius (Equ.2) = %.2e %s\n' % (self.radius['val']['b'],
                                              self.radius['unit']))
        add('\tRadius (Polar) = %.2e %s\n' % (self.radius['val']['c'],
                                              self.radius['unit']))
        add('\tFlattening     = %.2e %s\n' % (self.flattening()['val'],
                                              self.flattening()['unit']))
        add('\tEllipticity    = %.2e %s\n' % (self.ellipticity()['val'],
                                              self.ellipticity()['unit']))
        add('\tSurface Area   = %.2e %s\n' % (self.area()['val'],
                                              self.area()['unit']))
        add('\tVolume         = %.2e %s\n' % (self.volume()['val'],
                                              self.volume()['unit']))
        add('\tDensity        = %.2e %s\n' % (self.density()['val'],
                                              self.density()['unit']))
        add('\tMean Gravity   = %.2e %s\n' % (self.gravity_mean()['val'],
                                              self.gravity_mean()['unit']))
        add('\n')
        add('\t[Orbital Properties]\n')
        add('\tRotation Period    = %.2e %s\n' % (self.rotation['val'],
                                                  self.rotation['unit']))
        add('\tRotation Axis Tilt = %.2e %s\n' % (self.axtilt['val'],
                                                  self.axtilt['unit']))
        add('\tPeriapsis          = %.2e %s\n' % (self.periapsis['val'],
                                                  self.periapsis['unit']))
        add('\tApoapsis           = %.2e %s\n' % (self.apoapsis['val'],
                                                  self.apoapsis['unit']))
        add('\tSemi-Major axis    = %.2e %s\n' % (self.semimaj['val'],
                                                  self.semimaj['unit']))
        add('\tOrbit Inclination  = %.2e %s\n' % (self.inclination['val'],
                                                  self.inclination['unit']))
        add('\tPeriapsis Argument = %.2e %s\n' % (self.periarg['val'],
                                                  self.periarg['unit']))
        add('\tAscending Node     = %.2e %s\n' % (self.ascnode['val'],
                                                  self.ascnode['unit']))
        
        out = "".join(buff)
        print(out)

  
