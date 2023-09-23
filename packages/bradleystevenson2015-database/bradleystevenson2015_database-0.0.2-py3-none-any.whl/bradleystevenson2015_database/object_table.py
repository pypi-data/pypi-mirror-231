from table import Table


class ObjectTable(Table):


    def __init__(self, database, table_name, columns):
        super().__init__(database, table_name, columns.extend(['id']))

