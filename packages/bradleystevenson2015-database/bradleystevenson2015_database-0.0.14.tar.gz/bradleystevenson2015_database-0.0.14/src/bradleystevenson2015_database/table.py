class Table(object):

    def __init__(self, database, table_name, columns):
        self.database = database
        self.table_name = table_name
        self.columns = columns
        self.data = []


    def generate_from_database(self):
        self.data = self.database.execute_select_statement(self._generate_select_all_string())


    def append(self, insert_dict):
        new_dict = {}
        for column in self.columns:
            new_dict[column] = insert_dict[column]
        self.data.append(new_dict)


    def _generate_select_all_string(self):
        return_string = 'SELECT '
        for column in self.columns:
            return_string += column + ', '
        return_string = return_string[:-2] + ' FROM ' + self.table_name



class ObjectTable(Table):


    def __init__(self, database, table_name, columns):
        new_columns = columns.extend(['id'])
        super().__init__(database, table_name, new_columns)
        self.max_id = 1


    def generate_from_database(self):
        super().generate_from_database()
        self.max_id = self.database.execute_select_statement('SELECT MAX(id) FROM ' + self.table_name, 'id')[0]['id']


    def append(self, insert_dict):
        insert_dict['id'] = self.max_id
        self.max_id += 1
        super().append(insert_dict)