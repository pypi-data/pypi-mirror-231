import sqlite3
import os
import json
from table import Table

class Database:

    def __init__(self, database_path, schema_path):
        self.conn = sqlite3.connect(database_path)
        self.database_path = database_path
        self.schema_path = schema_path
        self._create_tables()

    def delete_database(self):
        self.conn.close()
        os.remove(self.database_path)
        self.conn = sqlite3.connect(self.database_path)


    def execute(self, execution_string):
        self.conn.execute(execution_string)
        self.conn.commit()


    def execute_select_statement(self, select_statement, columns):
        cursor = self.conn.cursor()
        cursor.execute(select_statement)
        return_list = []
        for data in cursor.fetchall():
            return_dict = {}
            inx = 0
            for column in columns:
                return_dict[column] = data[inx]
                inx += 1
            return_list.append(return_dict)
        return return_list

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