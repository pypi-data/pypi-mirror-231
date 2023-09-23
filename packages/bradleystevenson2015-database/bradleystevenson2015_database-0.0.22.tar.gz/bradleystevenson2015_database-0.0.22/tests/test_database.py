import unittest
import sys
sys.path.insert(0, '/Users/bradleystevenson/Programs/python-database-wrapper/src/bradleystevenson2015_database')

from database import Database

class TestDatabase(unittest.TestCase):

    def test_initialization(self):
        database = Database("../../databases/python-database-wrapper-test.db", "test-schema.json")
        database.create_tables()
        self.assertEquals(len(database.tables.keys()), 1)

    def test_select_string_generation(self):
        database = Database("../../databases/python-database-wrapper-test.db", "test-schema.json")
        database.create_tables()
        database.tables['test-table'].append({'column': 'test'})
        self.assertEquals('INSERT INTO test-table (column) VALUES ("test") ', database.tables['test-table']._generate_insert_string())

if __name__ == '__main__':
    unittest.main()