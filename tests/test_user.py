import unittest
import psycopg2
from models.user import User



class TestUser(unittest.TestCase):


    def setUp(self):
        self.user = User()
        self.connect = User.connect_db(self)
        self.cursor = self.connect.cursor()


    def test_connect_db(self):
        response = self.user.connect_db()
        connection = psycopg2.connect(user='mac', password=None, host='127.0.0.1', port='5432', database='test_script')
        result_1 = response.get_dsn_parameters()
        result_2 = connection.get_dsn_parameters()
        self.assertEqual(result_1, result_2)

    def test_load_schema_file(self):
        response = self.user.load_schema_file()
        result = "Tables created successfully in PostgreSQL"
        self.assertEqual(response, result)

    def test_load_seeder_file(self):
        self.user.load_schema_file()
        response = self.user.load_seeder_file()
        result = "Tables populated successfully in PostgreSQL"
        self.assertEqual(response, result)

    def test_display_table_content(self):
        response = self.user.display_table_content()
        result = len(response)
        self.assertEqual(result, 10)

    def test_all(self):
        response = self.user.all()
        result = len(response)
        self.assertEqual(result, 10)

    def test_get(self):
        id = 10
        response = self.user.get(id)
        self.assertIsInstance(response, tuple)

    def test_create(self):
        total_record = 10
        self.user.create(15, 'Charissa', 'Crighton', '2020/8/13', '2021/2/14')
        self.connect.commit()
        response = self.user.display_table_content()
        result = len(response)
        self.assertEqual(result, total_record + 1)

    def test_update(self):
        id = 6
        response_1 = self.user.get(id)
        self.user.update(6, 'Charissa', 'Crighton', '2020/8/13', '2021/2/14')
        response_2 = self.user.get(id)
        self.assertEqual(len(response_1), len(response_2))
        self.assertIsInstance(response_1, tuple)

    def test_delete(self):
        total_record = 10
        id = 10
        self.user.delete(id)
        self.connect.commit()
        response = self.user.display_table_content()
        result = len(response)
        self.assertEqual(result, total_record - 1)

    def tearDown(self):
        user = User()
        self.close = user.close_db_connections()

if __name__ == '__main__':
    unittest.main()