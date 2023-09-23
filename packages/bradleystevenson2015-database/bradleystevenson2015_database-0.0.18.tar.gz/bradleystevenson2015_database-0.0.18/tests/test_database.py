import unittest
import sys
sys.path.insert(0, '/Users/bradleystevenson/Programs/python-database-wrapper/src/bradleystevenson2015_database')

from database import Database

class TestDatabase(unittest.TestCase):

    def test_initialization(self):
        database = Database("../../databases/python-database-wrapper-test.db", "test-schema.json")
        database.create_tables()
        self.assertEquals(len(database.tables.keys()), 1)

if __name__ == '__main__':
    unittest.main()