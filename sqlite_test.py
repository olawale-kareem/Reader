import unittest
import sqlite3
from sqlite_main import SqlDb



class TestUser(unittest.TestCase):

    def setUp(self):
        self.operation = SqlDb()

    def test_connect(self):
        conn, cur = self.operation.connection()
        response = self.operation.test_connect()
        sqlite_query = 'SELECT sqlite_version();'
        cur.execute(sqlite_query)
        record = cur.fetchall()
        self.assertEqual(record,response)

    def test_create_record(self):
        response = self.operation.create_record('Buff', 'Bif', '632-79-9939', 46.0, 20.0, 30.0, 40.0, 50.0, 'B+')
        self.assertEqual(response, 'Record Successfully Created')

    def test_read_all_records(self):
        response = self.operation.read_all_records()
        total_records = 16
        result = len(response)
        self.assertEqual(result, total_records)




    def tearDown(self):
        operation = SqlDb()
        self.close = operation.close_connection()

    if __name__ == '__main__':
        unittest.main()
