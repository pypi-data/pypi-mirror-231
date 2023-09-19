from .LogicElement import LogicElement
from .LogicOperand import LogicOperand
from .LogicOperator import LogicOperator
from .operators import *

LOGIC_OPERATORS = sorted([
    Or, And,
    Equal, Unequal,
    GreaterThan, GreaterThanEqual, LessThan, LessThanEqual,
    ArrowLeft,
    Add, Minus, Multiply, Divide
], key=lambda x: x.order, reverse=True)
LOGIC_NOT = Not
