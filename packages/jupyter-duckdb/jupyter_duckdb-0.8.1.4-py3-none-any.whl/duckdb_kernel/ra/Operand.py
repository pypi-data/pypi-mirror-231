from typing import Dict, Tuple, Iterator

from duckdb_kernel.db import Table
from .Element import Element
from .util.RenamableColumnList import RenamableColumnList


class Operand(Element):
    def __init__(self, relation: str):
        self.relation: str = relation

    def __str__(self, indent: int = 0) -> str:
        return f'{super().__str__(indent)}: {self.relation}'

    @property
    def name(self) -> str:
        return self.relation

    @property
    def children(self) -> Iterator['Element']:
        return
        yield

    def to_sql(self, tables: Dict[str, Table]) -> Tuple[str, RenamableColumnList]:
        if self.relation not in tables:
            raise AssertionError(f'unknown relation {self.relation}')

        cols = RenamableColumnList.from_iter(tables[self.name].columns)
        column_names = ', '.join(c.rename() for c in cols)

        return f'SELECT DISTINCT {column_names} FROM {self.relation}', cols
