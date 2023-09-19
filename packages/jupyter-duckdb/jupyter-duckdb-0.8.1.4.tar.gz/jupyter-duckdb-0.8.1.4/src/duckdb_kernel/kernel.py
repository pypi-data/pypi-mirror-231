import json
import math
import os
import time
import traceback
from typing import Optional, Dict, List, Tuple

import duckdb
from ipykernel.kernelbase import Kernel

from .db import analyze_db
from .magics import *
from .ra import RA
from .util.ResultSetComparator import ResultSetComparator
from .util.formatting import row_count, rows_table, wrap_image
from .visualization import *


class DuckDBKernel(Kernel):
    DEFAULT_MAX_ROWS = 20

    implementation = 'DuckDB'
    implementation_version = '0.8.1'
    banner = 'DuckDB Kernel'
    language_info = {
        'name': 'duckdb',
        'mimetype': 'application/sql',
        'file_extension': '.sql',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # register magic commands
        self._magics: MagicCommandHandler = MagicCommandHandler()

        self._magics.add(
            MagicCommand('create').arg('database').opt('of').opt('with_tests').on(self._create_magic),
            MagicCommand('load').arg('database').opt('with_tests').on(self._load_magic),
            MagicCommand('test').arg('name').result(True).on(self._test_magic),
            MagicCommand('all', 'all_rows').on(self._all_magic),
            MagicCommand('max_rows').arg('count').on(self._max_rows_magic),
            MagicCommand('query_max_rows').arg('count').on(self._query_max_rows_magic),
            MagicCommand('schema').flag('td').on(self._schema_magic),
            MagicCommand('ra').flag('analyze').code(True).on(self._ra_magic)
        )

        # create placeholders for database and tests
        self._db: Optional[duckdb.DuckDBPyConnection] = None
        self._tests: Optional[Dict] = None

    # output related functions
    def print(self, text: str, name: str = 'stdout'):
        self.send_response(self.iopub_socket, 'stream', {
            'name': name,
            'text': text
        })

    def print_exception(self, e: Exception):
        if isinstance(e, AssertionError):
            text = str(e)
        elif isinstance(e, MagicCommandException):
            text = str(e)
        elif isinstance(e, (duckdb.OperationalError, duckdb.ProgrammingError, duckdb.InvalidInputException)):
            text = str(e)

            # ignore InvalidInputException if an empty query was executed
            if text == 'Invalid Input Error: No open result set':
                return
        else:
            text = traceback.format_exc()

        self.print(text, 'stderr')

    def print_data(self, *data: str, mime: str = 'text/html'):
        for v in data:
            self.send_response(self.iopub_socket, 'display_data', {
                'data': {
                    mime: v
                },
                # `metadata` is required. Otherwise, Jupyter Lab does not display any output.
                # This is not the case when using Jupyter Notebook btw.
                'metadata': {}
            })

    # database related functions
    def _load_database(self, database: str, read_only: bool):
        if self._db is None:
            self._db = duckdb.connect(database, read_only)
            return True
        else:
            return False

    def _unload_database(self):
        if self._db is not None:
            self._db.close()
            self._db = None
            return True
        else:
            return False

    def _execute_stmt(self, query: str, silent: bool,
                      max_rows: Optional[int]) -> Tuple[Optional[List[str]], Optional[List[List]]]:
        if self._db is None:
            raise AssertionError('load a database first')

        with self._db.cursor() as cursor:
            # execute query and store start and end timestamp
            st = time.time()
            cursor.execute(query)
            et = time.time()

            if not silent:
                # print EXPLAIN queries as raw text
                if query.strip().startswith('EXPLAIN'):
                    rows = cursor.fetchall()
                    for ekey, evalue in rows:
                        self.print_data(f'<b>{ekey}</b><br><pre>{evalue}</pre>')

                    return None, None

                # print every other query as a table
                else:
                    # table header
                    if cursor.description is None:
                        columns = []
                    else:
                        columns = [e[0] for e in cursor.description]

                    table_header = ''.join(f'<th>{c}</th>' for c in columns)

                    # table data
                    rows = cursor.fetchall()

                    if max_rows is not None and len(rows) > max_rows:
                        table_data = f'''
                            {rows_table(rows[:math.ceil(max_rows / 2)])}
                            <tr>
                                <td colspan="{len(columns)}" 
                                    style="text-align: center"
                                    title="{row_count(len(rows) - max_rows)} omitted">
                                    ...
                                </td>
                            </tr>
                            {rows_table(rows[-math.floor(max_rows // 2):])}
                        '''
                    else:
                        table_data = ''.join(map(
                            lambda row: '<tr>' + ''.join(map(lambda e: f'<td>{e}</td>', row)) + '</tr>',
                            rows
                        ))

                    # send to client
                    self.print_data(f'''
                        <table class="duckdb-query-result">
                            {table_header}
                            {table_data}
                        </table>
                    ''')

                    self.print_data(f'{row_count(len(rows))} in {et - st:.3f}s')

            return columns, rows

    # magic command related functions
    def _create_magic(self, silent: bool, path: str, of: Optional[str], with_tests: Optional[str]):
        self._load(silent, path, True, of, with_tests)

    def _load_magic(self, silent: bool, path: str, with_tests: Optional[str]):
        self._load(silent, path, False, None, with_tests)

    def _load(self, silent: bool, path: str, create: bool, of: Optional[str], with_tests: Optional[str]):
        # unload current database if necessary
        if self._unload_database():
            if not silent:
                self.print('unloaded database\n')

        # print kernel version
        if not silent:
            self.print(f'{self.implementation} {self.implementation_version}\n')

        # clean path
        if path.startswith(("'", '"')):
            path = path[1:]
        if path.endswith(("'", '"')):
            path = path[:-1]

        # load new database
        if create and os.path.exists(path):
            os.remove(path)

        if self._load_database(path, read_only=False):
            if not silent:
                self.print(f'loaded database "{path}"\n')

        # copy data from source database
        if of is not None:
            # clean path
            if of.startswith(("'", '"')):
                of = of[1:]
            if of.endswith(("'", '"')):
                of = of[:-1]

            # load sql files
            if of.endswith('.sql'):
                with open(of, 'r') as file:
                    content = file.read()

                    # statements = re.split(r';\r?\n', content)
                    # for statement in statements:
                    #     self._db.execute(statement)

                    self._db.execute(content)

                    if not silent:
                        self.print(f'executed "{of}"\n')

            # load database files
            else:
                with duckdb.connect(of, read_only=True) as of_db:
                    of_db.execute('SHOW TABLES')
                    for table, in of_db.fetchall():
                        transfer_df = of_db.query(f'SELECT * FROM {table}').to_df()
                        self._db.execute(f'CREATE TABLE {table} AS SELECT * FROM transfer_df')

                        if not silent:
                            self.print(f'transferred table {table}\n')

        # load tests
        if with_tests is None:
            self._tests = {}
        else:
            with open(with_tests, 'r') as tests_file:
                self._tests = json.load(tests_file)
                self.print(f'loaded tests from {with_tests}\n')

    def _test_magic(self, silent: bool, _: List[str], result: List[List], name: str):
        # Testing makes no sense if there is no output.
        if silent:
            return

        # extract data for test
        data = self._tests[name]

        # ordered test
        if data['ordered']:
            # calculate diff
            rsc = ResultSetComparator(result, data['equals'])

            missing = len(rsc.ordered_right_only)
            if missing > 0:
                return self.print_data(wrap_image(False, f'{row_count(missing)} missing'))

            missing = len(rsc.ordered_left_only)
            if missing > 0:
                return self.print_data(wrap_image(False, f'{row_count(missing)} more than required'))

            return self.print_data(wrap_image(True))

        # unordered test
        else:
            # calculate diff
            rsc = ResultSetComparator(result, data['equals'])

            below = len(rsc.right_only)
            above = len(rsc.left_only)

            # print result
            if below > 0 and above > 0:
                self.print_data(wrap_image(False, f'{row_count(below)} missing, {row_count(above)} unnecessary'))
            elif below > 0:
                self.print_data(wrap_image(False, f'{row_count(below)} missing'))
            elif above > 0:
                self.print_data(wrap_image(False, f'{row_count(above)} unnecessary'))
            else:
                self.print_data(wrap_image(True))

    def _all_magic(self, silent: bool):
        return {
            'max_rows': None
        }

    def _max_rows_magic(self, silent: bool, count: str):
        if count.lower() != 'none':
            DuckDBKernel.DEFAULT_MAX_ROWS = int(count)
        else:
            DuckDBKernel.DEFAULT_MAX_ROWS = None

    def _query_max_rows_magic(self, silent: bool, count: str):
        return {
            'max_rows': int(count) if count.lower() != 'none' else None
        }

    def _schema_magic(self, silent: bool, td: bool):
        if silent:
            return

        # analyze tables
        tables = analyze_db(self._db)

        # create and show visualization
        vd = SchemaDrawer(list(tables.values()))
        svg = vd.to_svg(not td)

        self.print_data(svg)

    def _ra_magic(self, silent: bool, code: str, analyze: bool):
        if silent:
            return

        if not code.strip():
            return

        # analyze tables
        tables = analyze_db(self._db)

        # parse ra input
        root_node = RA.parse(code)

        # create and show visualization
        if analyze:
            vd = RATreeDrawer(self._db, root_node, tables)
            svg = vd.to_svg(True)

            self.print_data(svg)

        # generate sql
        sql = root_node.to_sql_with_renamed_columns(tables)

        return {
            'generated_code': sql
        }

    # jupyter related functions
    def do_execute(self, code: str, silent: bool,
                   store_history: bool = True, user_expressions: dict = None, allow_stdin: bool = False,
                   **kwargs):
        try:
            # get magic command
            clean_code, pre_query_callbacks, post_query_callbacks = self._magics(silent, code)

            # execute magic commands here if it does not depend on query results
            execution_args = {
                'max_rows': DuckDBKernel.DEFAULT_MAX_ROWS
            }

            for callback in pre_query_callbacks:
                execution_args.update(callback())

            # overwrite clean_code with generated code
            if 'generated_code' in execution_args:
                clean_code = execution_args['generated_code']
                del execution_args['generated_code']

            # execute statement if needed
            if clean_code.strip():
                cols, rows = self._execute_stmt(clean_code, silent, **execution_args)
            else:
                cols, rows = None, None

            # execute magic command here if it does depend on query results
            for callback in post_query_callbacks:
                callback(cols, rows)

            return {
                'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {}
            }

        except Exception as e:
            self.print_exception(e)

            return {
                'status': 'error',
                'ename': str(type(e)),
                'evalue': str(e),
                'traceback': traceback.format_exc()
            }

    def do_shutdown(self, restart):
        self._unload_database()
        return super().do_shutdown(restart)
