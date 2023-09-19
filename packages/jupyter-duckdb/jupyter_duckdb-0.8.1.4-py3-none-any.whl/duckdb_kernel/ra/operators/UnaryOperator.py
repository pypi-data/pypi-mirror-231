from typing import Iterator

from ..Element import Element
from ..Operator import Operator
from ..logic import LogicElement


class UnaryOperator(Operator):
    def __init__(self, target: Element):
        self.target: Element = target

    @property
    def arg(self) -> LogicElement:
        raise NotImplementedError

    @property
    def conditions(self) -> str:
        return str(self.arg)

    def __str__(self, indent: int = 0) -> str:
        return f'{super().__str__(indent)} with arg=({self.arg})\n{self.target.__str__(indent + 1)}'

    @property
    def children(self) -> Iterator['Element']:
        yield self.target
