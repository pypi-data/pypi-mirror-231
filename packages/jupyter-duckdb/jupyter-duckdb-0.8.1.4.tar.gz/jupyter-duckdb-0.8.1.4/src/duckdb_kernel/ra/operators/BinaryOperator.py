from typing import Iterator

from .. import Element
from ..Operator import Operator


class BinaryOperator(Operator):
    def __init__(self, left: Element, right: Element):
        self.left: Element = left
        self.right: Element = right

    def __str__(self, indent: int = 0) -> str:
        return f'{super().__str__(indent)}\n{self.left.__str__(indent + 1)}\n{self.right.__str__(indent + 1)}'

    @property
    def children(self) -> Iterator['Element']:
        yield self.left
        yield self.right
