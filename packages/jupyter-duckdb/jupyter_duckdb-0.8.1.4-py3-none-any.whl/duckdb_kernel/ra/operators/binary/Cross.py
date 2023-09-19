from typing import Tuple, Dict

from duckdb_kernel.db import Table
from .. import BinaryOperator
from .. import RenamableColumnList


class Cross(BinaryOperator):
    @staticmethod
    def symbols() -> Tuple[str, ...]:
        return chr(215), 'x'

    def to_sql(self, tables: Dict[str, Table]) -> Tuple[str, RenamableColumnList]:
        # execute subqueries
        lq, lcols = self.left.to_sql(tables)
        rq, rcols = self.right.to_sql(tables)

        # merge columns
        cols = lcols.merge(rcols)

        # create statement
        return f'SELECT {cols.list} FROM ({lq}) {self._name()} CROSS JOIN ({rq}) {self._name()}', cols
