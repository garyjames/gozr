# mydb.py
"""db server connection"""

import pyodbc
from exceptions import StandardError
from collections import namedtuple
import mydsn as dsn

class MyDB(object):
    """more info at https://www.python.org/dev/peps/pep-0249"""

    apilevel = '2.0'
    threadsafety = 1
    paramstyle = 'pyformat'

    _tmps = 'Driver={{{driver}}};Server={server};Database={database};Uid={uid};Pwd={pwd}'

    def __init__(self, db_alias):
        self._dsn = _tmps.format(**dsn.dsn(db_alias))
        self._cnxn = pyodbc.connect(self._dsn)
        self._cursor = self._cnxn.cursor()

    def __del__(self):
        self._cnxn.close()

    def query(self, query, params):
        return self._cursor.execute(query, params)

    @property
    def databases(self):
        return self._cursor.execute("select name from master..sysdatabases")

    @property
    def tables(self):
        if self._db:
            return self.query(
                "select table_name from %(db)s.information_schema.tables " +
                "where table_type = 'BASE TABLE'", db=self._db)

#    def query(self, query=None, ret_as_tuple=True):
#        """return either a cursor or a generator which yields named tuples"""
#        records = self.cursor.execute(query)
#        if query and ret_as_tuple:
#            column_names = [ i[0] for i in records.description ]
#            named_row = namedtuple('named_row', column_names)
#            return ( named_row._make(i) for i in records )
#        elif query:
#            return records
