import unittest
import psycopg2
from models.books import Book


class TestBooks(unittest.TestCase):

    def setUp(self):
        self.book = Book()
        self.connect = Book.connect_db(self)
        self.cursor = self.connect.cursor()

    def test_connect_db(self):
        response = self.book.connect_db()
        connection = psycopg2.connect(user='mac', password=None, host='127.0.0.1', port='5432', database='test_script')
        result_1 = response.get_dsn_parameters()
        result_2 = connection.get_dsn_parameters()
        self.assertEqual(result_1, result_2)

    def test_load_schema_file(self):
        response = self.book.load_schema_file()
        result = "Tables created successfully in PostgreSQL"
        self.assertEqual(response, result)

    def test_load_seeder_file(self):
        self.book.load_schema_file()
        response = self.book.load_seeder_file()
        result = "Tables populated successfully in PostgreSQL"
        self.assertEqual(response, result)

    def test_display_table_content(self):
        response = self.book.display_table_content()
        result = len(response)
        self.assertEqual(result, 10)

    def test_all(self):
        response = self.book.all()
        result = len(response)
        self.assertEqual(result, 10)




    def tearDown(self):
        user = Book()
        self.close = user.close_db_connections()

if __name__ == '__main__':
    unittest.main()
