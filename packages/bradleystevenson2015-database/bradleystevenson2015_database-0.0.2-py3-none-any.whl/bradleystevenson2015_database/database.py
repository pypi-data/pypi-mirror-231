import sqlite3
import os
import json
from table import Table

class Database:

    def __init__(self, database_path, schema_path):
        self.conn = sqlite3.connect(database_path)
        self.database_path = database_path
        self.schema_path = schema_path

    def delete_database(self):
        self.conn.close()
        os.remove(self.database_path)
        self.conn = sqlite3.connect(self.database_path)


    def _create_tables(self):
        schema_file = open(self.schema_path)
        data = json.load(schema_file)
        schema_file.close()
        self.tables = {}
        for table in data['tables']:
            if table['table_type'] == 'table':
                self.tables[table['table_name']] = Table(self, table['table_name'], table['columns'])
            elif table['table_type'] == 'object_table':
                self.tables[table['table_name']] = Table(self, table['table_name'], table['columns'])
            else:
                raise Exception("NO match for table type")