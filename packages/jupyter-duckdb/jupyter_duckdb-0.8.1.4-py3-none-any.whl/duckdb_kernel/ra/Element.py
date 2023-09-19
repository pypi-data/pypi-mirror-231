from typing import Dict, Tuple, Iterator, Optional

from duckdb_kernel.db import Table
from .util.RenamableColumnList import RenamableColumnList


class Element:
    __COUNTER = 0

    @staticmethod
    def _name() -> str:
        Element.__COUNTER += 1
        return f'__t{Element.__COUNTER:06}'

    def __str__(self, indent: int = 0) -> str:
        return ('   ' * indent) + self.__class__.__name__

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def children(self) -> Iterator['Element']:
        raise NotImplementedError

    @property
    def conditions(self) -> Optional[str]:
        return None

    def to_sql(self, tables: Dict[str, Table]) -> Tuple[str, RenamableColumnList]:
        raise NotImplementedError

    def to_sql_with_renamed_columns(self, tables: Dict[str, Table]) -> str:
        sql, columns = self.to_sql(tables)
        column_names = ', '.join(f"{c.current_name} AS '{c.full_name}'" for c in columns)

        return f'SELECT {column_names} FROM ({sql}) {self._name()}'

    def to_sql_with_count(self, tables: Dict[str, Table]) -> str:
        sql, _ = self.to_sql(tables)
        return f'SELECT COUNT(*) FROM ({sql}) {self._name()}'
