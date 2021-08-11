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

    def test_read_by_SSN(self):
        conn, cur = self.operation.connection()
        SSN = 10
        response = self.operation.read_records_by_SSN(SSN)
        sql_read_query = f"SELECT * FROM grades WHERE SSN = '{SSN}'"
        cur.execute(sql_read_query)
        records = cur.fetchone()
        self.assertEqual(response, records)

    def test_update_records(self):
        response = self.operation.update_record('632-79-9939', '632-79-9939', 46.0, 20.0, 30.0, 60.0, 70.0, 'A+')
        self.assertEqual(response, "Record updated successfully in users table")

    def test_final_50_and_above(self):
        total_records_50_and_above = 5
        response = self.operation.final_50_and_above()
        result = len(response)
        self.assertEqual(result, total_records_50_and_above)

    def tearDown(self):
        operation = SqlDb()
        self.close = operation.close_connection()

    if __name__ == '__main__':
        unittest.main()
