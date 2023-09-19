from .Cross import Cross
from .Difference import Difference
from .Intersection import Intersection
from .Join import Join
from .Union import Union

# inverse binding strength
BINARY_OPERATORS = [
    Difference,
    Union,
    Intersection,
    Join,
    Cross
]
