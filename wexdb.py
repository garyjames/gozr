# wexdb.py
"""db server connection"""

import pyodbc
from collections import namedtuple

class Wexdb(object):
    def __init__(self, dbServerName):
        cnxn = connect(dbServerName)
        self.cursor = cnxn.cursor()

    @property
    def databases(self):
        return self.query("select name from master..sysdatabases")

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


def connect(server=None):

    db_params = dict()

    connection_string = ('DRIVER={driver}; SERVER={server}; UID={username}; PWD={password}')

    db_params['wt-woman'] = {
        'driver': '{SQL Server}',
        'server': 'wt-woman',
        'username': 'wexreports',
        'password': 'R3p0rtl+'
    }

    db_params['wxsec-dbmarley'] = {
        'driver': '{SQL Server}',
        'server': 'wxsec-dbmarley',
        'username': 'wexreports',
        'password': 'R3p0rtl+'
    }

    db_params[r'wtdb5\dev5'] = {
        'driver': '{SQL Server}',
        'server': r'WTDB5\DEV5',
        'username': 'Mod6',
        'password': 'Mod6'
    }

    db_params[r'wt-chsql1'] = {
        'driver': '{SQL Server}',
        'server': r'wt-chsql1',
        'username': 'wexreports',
        'password': 'R3p0rtl+'
    }

    db_params['dbtest'] = {
        'driver': '{SQL Server}',
        'server': 'wt-dbtest',
        'username': 'wexreports',
        'password': 'R3p0rtl+'
    }

    if server:
        return pyodbc.connect(connection_string.format(**db_params[server]))
