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

#Display Earth volume
In [1]: earth.volume()
Out[1]: {'unit': 'm^{-3}', 'val': 1.0832072662532028e+21}

# Display Europa mass related to Earth
In [2]: europa.mass['val']/earth.mass['val']
Out[2]: 0.00803691778058
```

  [1]: https://en.wikipedia.org/?title=International_System_of_Units
