from .Projection import Projection
from .Rename import Rename
from .Selection import Selection

# inverse binding strength
UNARY_OPERATORS = [
    Projection,
    Rename,
    Selection
]
