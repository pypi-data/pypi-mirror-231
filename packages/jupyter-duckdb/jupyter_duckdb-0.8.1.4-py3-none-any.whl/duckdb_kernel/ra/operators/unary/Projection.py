from typing import Dict, Tuple

from duckdb_kernel.db import Table
from .. import Element, RenamableColumnList, LogicOperand, LogicElement
from ..UnaryOperator import UnaryOperator


class Projection(UnaryOperator):
    @staticmethod
    def symbols() -> Tuple[str, ...]:
        return 'Π', 'π', 'pi'

    def __init__(self, target: Element, arg: LogicOperand):
        if not isinstance(arg, LogicOperand):
            raise AssertionError('only argument lists allowed as parameter')

        super().__init__(target)
        self.columns: LogicOperand = arg

    @property
    def arg(self) -> LogicElement:
        return self.columns

    def to_sql(self, tables: Dict[str, Table]) -> Tuple[str, RenamableColumnList]:
        # execute subquery
        subquery, subcols = self.target.to_sql(tables)

        # map names to columns from subquery
        cols = subcols.filter(*(name.clean for name in self.columns))

        # get sql
        return f'SELECT DISTINCT {cols.list} FROM ({subquery}) {self._name()}', cols
