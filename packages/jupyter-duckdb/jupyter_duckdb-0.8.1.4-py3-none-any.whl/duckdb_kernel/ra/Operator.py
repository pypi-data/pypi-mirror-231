from typing import Tuple

from .Element import Element


class Operator(Element):
    @staticmethod
    def symbols() -> Tuple[str, ...]:
        raise NotImplementedError

    @property
    def name(self) -> str:
        return self.symbols()[0]
