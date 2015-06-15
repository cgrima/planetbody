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
In [1]: mars.nfo.radius
Out[1]: {'a': 3396200.0, 'b': 3396200.0, 'c': 3376200.0}

# Display Europa mass related to Earth
In [2]: europa.nfo.mass/earth.nfo.mass
Out[2]: 0.00803691778058
```

  [1]: https://en.wikipedia.org/?title=International_System_of_Units
