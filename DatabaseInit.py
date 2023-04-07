import sqlite3


class databaseInit:
    def __init__(self, database):
        self.var = None
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table, *values):
        self.cursor.execute(f'INSERT INTO {table} (name, surrname) VALUES (?,?)', values)
        self.connection.commit()

    def returnRecords(self, table):
        self.cursor.execute(f'SELECT name, surrname FROM {table}')
        self.var = self.cursor.fetchall()
        return self.var