# mydb.py
"""db server connection"""

import pyodbc
from collections import namedtuple
import utilities as utils

pyodbc.paramstyle = 'pyformat'

class mydb(object):
    """more info at https://www.python.org/dev/peps/pep-0249"""

    def __init__(self, db_alias):
        tmp = 'Driver={{{driver}}};Database={database};Server={server};Uid={uid};Pwd={pwd}'
        ret = utils.dsn(db_alias)
        self._dsn = tmp.format(**ret)
        self._cnxn = pyodbc.connect(self._dsn)
        self._cursor = self._cnxn.cursor()
        self._db = self._cnxn.getinfo(pyodbc.SQL_DATABASE_NAME)
        self._server = self._cnxn.getinfo(pyodbc.SQL_SERVER_NAME)
        self._username = self._cnxn.getinfo(pyodbc.SQL_USER_NAME)

    def __del__(self):
        self._cnxn.close()

    def query(self, query):
        return self._cursor.execute(query)

    @property
    def cursor(self):
        return self._cursor

    @property
    def username(self):
        self._username = self._cnxn.getinfo(pyodbc.SQL_USER_NAME)
        return self._username

    @property
    def server(self):
        self._server = self._cnxn.getinfo(pyodbc.SQL_SERVER_NAME)
        return self._server

    @property
    def db(self):
        self._db = self._cnxn.getinfo(pyodbc.SQL_DATABASE_NAME)
        return self._db

    @db.setter
    def db(self, d):
        self._cursor.execute("use {}".format(d))
        return self._cnxn.getinfo(pyodbc.SQL_DATABASE_NAME)

    @property
    def rowcount(self):
        return self._cursor.rowcount

    @property
    def description(self):
        return self._cursor.description

    @property
    def databases(self):
        return self._cursor.execute("select name from master..sysdatabases")

    @property
    def tables(self):
        q = ("select table_name from {}.information_schema.tables "
             "where table_type = 'BASE TABLE'")
        return self.query(q.format(self._db))

#    def query(self, query=None, ret_as_tuple=True):
#        """return either a cursor or a generator which yields named tuples"""
#        records = self.cursor.execute(query)
#        if query and ret_as_tuple:
#            column_names = [ i[0] for i in records.description ]
#            named_row = namedtuple('named_row', column_names)
#            return ( named_row._make(i) for i in records )
#        elif query:
#            return records

def firms(cnxn):
    q = r"select * from firms"
    return cnxn.query(q)
