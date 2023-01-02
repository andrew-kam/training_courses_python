import excep

print(excep.greet('Stud'))

import sys

for path in sys.path:
    print(path)

from excep import BadName, greet as exc_greet

print(BadName)
print(exc_greet)
