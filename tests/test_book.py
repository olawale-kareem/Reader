import unittest
import psycopg2
from models.book import Book


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

    def test_get(self):
        id = 10
        response = self.book.get(id)
        result = len(response)
        self.assertEqual(result, 7)
        self.assertIsInstance(response, tuple)

    def test_create(self):
        total_record = 10
        self.book.create(64, 3, 'Glad', 500, '2020-06-28', '2021-06-28')
        self.connect.commit()
        response = self.book.display_table_content()
        result = len(response)
        self.assertEqual(result, total_record + 1)

    def test_update(self):
        id = 6
        response_1 = self.book.get(id)
        self.book.update(6, 6, 'Purpose', 500, '2019-06-14', '2021-01-28')
        response_2 = self.book.get(id)
        self.assertEqual(len(response_1), len(response_2))
        self.assertIsInstance(response_1, tuple)
        self.assertIsInstance(response_2, tuple)

    def test_destroy(self):
        total_record = 10
        id = 10
        self.book.destroy(id)
        self.connect.commit()
        response = self.book.display_table_content()
        result = len(response)
        self.assertEqual(result, total_record - 1)

    def destroy(self, id):
        print('Books table before deleting record')
        self.display_table_content()

        print('Table after deleting record:')
        delete_query = f'DELETE FROM books WHERE id = {id}'
        self.cursor.execute(delete_query)
        self.connection.commit()
        count = self.cursor.rowcount

        self.display_table_content()
        print(count, "Record deleted successfully in books table")

    def tearDown(self):
        user = Book()
        self.close = user.close_db_connections()

if __name__ == '__main__':
    unittest.main()
