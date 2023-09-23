from table import Table


class ObjectTable(Table):


    def __init__(self, database, table_name, columns):
        super().__init__(database, table_name, columns.extend(['id']))
        self.max_id = 1


    def generate_from_database(self):
        super().generate_from_database()
        self.max_id = self.database.execute_select_statement('SELECT MAX(id) FROM ' + self.table_name, 'id')[0]['id']


    def append(self, insert_dict):
        insert_dict['id'] = self.max_id
        self.max_id += 1
        super().append(insert_dict)