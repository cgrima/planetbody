**Planetbody**
--
This is a Python package providing basic informations for some planetary bodies.
Units used are exclusively from the [International System of units][1].

**Usage example**
--
```
# Import package
from planetbody import earth, mars, europa

# Display Mars radiuses
In [1]: mars.radius
Out[1]: {'unit': 'm', 'val': {'a': 3396200.0, 'b': 3396200.0, 'c': 3376200.0}}

# Display Earth volume
In [2]: earth.volume()
Out[2]: {'unit': 'm^{-3}', 'val': 1.0832072662532028e+21}

# Display Europa mass related to Earth
In [3]: europa.mass['val']/earth.mass['val']
Out[3]: 0.00803691778058

#Display Mars Fact Sheet
In [3]: mars.report()
Mars (S IV) is a planet orbiting Sun

	[Physical Properties]
	Mass           = 6.42e+23 kg
	Radius (Mean)  = 3.39e+06 m
	Radius (Equ.1) = 3.40e+06 m
	Radius (Equ.2) = 3.40e+06 m
	Radius (Polar) = 3.38e+06 m
	Flattening     = 5.89e-03 None
	Ellipticity    = 1.08e-01 None
	Surface Area   = 1.44e+14 m^2
	Volume         = 1.63e+20 m^{-3}
	Density        = 3.93e+03 kg.m^{-3}
	Mean Gravity   = 3.73e+00 m.s^{-2}

	[Orbital Properties]
	Rotation Period    = 1.03e+00 days
	Rotation Axis Tilt = 2.52e+01 deg
	Periapsis          = 2.07e+11 m
	Apoapsis           = 2.49e+11 m
	Semi-Major axis    = 2.28e+11 m
	Orbit Inclination  = 1.85e+00 deg
	Periapsis Argument = 2.87e+02 deg
	Ascending Node     = 4.96e+01 deg
```

  [1]: https://en.wikipedia.org/?title=International_System_of_Units
