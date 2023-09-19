from typing import Dict

import duckdb
from graphviz import Digraph

from duckdb_kernel.db import Table
from duckdb_kernel.ra import Element
from .Drawer import Drawer
from duckdb_kernel.util.formatting import row_count


class RATreeDrawer(Drawer):
    def __init__(self, db: duckdb.DuckDBPyConnection, root_node: Element, tables: Dict[str, Table]):
        self.db: duckdb.DuckDBPyConnection = db
        self.root_node: Element = root_node
        self.tables: Dict[str, Table] = tables

    def to_graph(self) -> Digraph:
        # create graph
        ps = Digraph('Schema',
                     graph_attr={},
                     node_attr={
                         'shape': 'plaintext'
                     })

        # add nodes
        self.__add_node(ps, self.root_node)

        # return graph
        return ps

    def __add_node(self, ps: Digraph, node: Element) -> str:
        # use id of node object as identifier
        node_id = f'node_{id(node)}'

        # generate child nodes
        child_ids = [self.__add_node(ps, child) for child in node.children]

        # create node
        count_query = node.to_sql_with_count(self.tables)
        ((count,),) = self.db.execute(count_query).fetchall()

        if node.conditions is None:
            conditions = ''
        else:
            condition_str = node.conditions.replace('<', '&lt;').replace('>', '&gt;')
            conditions = f'<tr><td>{condition_str}</td></tr>'

        ps.node(
            node_id,
            f'''<
                <table border="0" cellborder="1" cellspacing="0" cellpadding="5">
                    <tr>
                        <td><b>{node.name}</b></td>
                    </tr>
                    
                    {conditions}
                    
                    <tr>
                        <td>{row_count(count)}</td>
                    </tr>
                </table>
            >'''
        )

        # add edges from node to children
        for child_id in child_ids:
            ps.edge(node_id, child_id, arrowhead='none')

        # return node identifier to generate edges
        return node_id
