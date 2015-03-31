# wexdb.py
"""db server connection"""

import pyodbc
from collections import namedtuple

class WexDB(object):
    def __init__(self, dsn='', user='', password='', host='', database=''):
        self._cnxn = pyodbc.connect(dsn, user, password, host, database)
        self._cursor = self._cnxn.cursor()

    def __del__(self):
        self._cnxn.close()

    @property
    def databases(self):
        return self._cursor.query("select name from master..sysdatabases")

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db):
        self.__db = db

    @property
    def tables(self):
        if self.__db:
            return self.query(
                "select table_name from {}.information_schema.tables ".format(self.__db) +
                "where table_type = 'BASE TABLE'")

    def query(self, query=None, ret_as_tuple=True):
        """return either a cursor or a generator which yields named tuples"""
        records = self.cursor.execute(query)
        if query and ret_as_tuple:
            column_names = [ i[0] for i in records.description ]
            named_row = namedtuple('named_row', column_names)
            return ( named_row._make(i) for i in records )
        elif query:
            return records

    def query(self, query, params):
        return self._cursor.execute(query, params)


def connect(server=None):

    db_params = dict()

    connection_string = ('DRIVER={driver}; SERVER={server}; UID={username}; PWD={password}')

    if server:
        return pyodbc.connect(connection_string.format(**db_params[server]))
