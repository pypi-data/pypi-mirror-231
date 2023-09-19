from typing import Dict, Tuple

from duckdb_kernel.db import Table
from .. import Element, RenamableColumnList, LogicElement
from ..UnaryOperator import UnaryOperator


class Selection(UnaryOperator):
    @staticmethod
    def symbols() -> Tuple[str, ...]:
        return 'σ', 'sigma'

    def __init__(self, target: Element, arg: LogicElement):
        super().__init__(target)
        self.condition = arg

    @property
    def arg(self) -> LogicElement:
        return self.condition

    def to_sql(self, tables: Dict[str, Table]) -> Tuple[str, RenamableColumnList]:
        # execute subquery
        subquery, subcols = self.target.to_sql(tables)

        # convert logic expression to sql
        condition = self.condition.to_sql(subcols)

        # return sql
        return f'SELECT {subcols.list} FROM ({subquery}) {self._name()} WHERE {condition}', subcols
