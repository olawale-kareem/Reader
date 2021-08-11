import psycopg2
from psycopg2 import DatabaseError as Error


class Book:
    def __init__(self):
        self.connection = self.connect_db()
        self.cursor = self.connect_db().cursor()
        self.schema_file = '/Users/mac/decagon_python_class/week6/schema.sql'
        self.seeder_file = '/Users/mac/decagon_python_class/week6/seeder.sql'


    def connect_db(self):
        try:
            connection = psycopg2.connect(user='mac', password=None, host='127.0.0.1', port='5432',
                                          database='test_script')
            return connection
        except (Exception, Error) as err:
            return f'Error while connecting to the PostgreSQL {err}'

    def load_schema_file(self):
        try:
            schema_file = open(self.schema_file, 'r')
            schema_file_content = schema_file.readlines()
            formatted_schema_file = ''.join(schema_file_content)
            self.cursor.execute(formatted_schema_file)
            self.connection.commit()
            schema_file.close()
            return "Tables created successfully in PostgreSQL"
        except (Exception, Error) as err:
            return f'Error while connecting to the PostgreSQL {err}'

    def load_seeder_file(self):
        try:
            seeder_file = open(self.seeder_file, 'r')
            seeder_file_content = seeder_file.readlines()
            formatted_seeder_file = ''.join(seeder_file_content)
            self.cursor.execute(formatted_seeder_file)
            self.connection.commit()
            seeder_file.close()
            return "Tables populated successfully in PostgreSQL"
        except (Exception, Error) as err:
            return f'Error while connecting to the PostgreSQL {err}'

    def display_table_content(self):
        db_query = f'SELECT * FROM books'
        self.cursor.execute(db_query)
        db_response = self.cursor.fetchall()
        print(
            f'-------------------------------------------- Table:books ---------------------------------------------\n')
        for row in db_response:
            print(row, '\n')
        return db_response

    def all(self):
        db_query = f'SELECT name FROM books'
        self.cursor.execute(db_query)
        db_response = self.cursor.fetchall()
        for row in db_response:
            print(row, '\n')
        return db_response

    def get(self, book_id):
        db_query = f'SELECT * FROM users WHERE id = {book_id}'
        self.cursor.execute(db_query)
        db_response = self.cursor.fetchone()
        print(db_response)
        return db_response

    def create(self, *args):
        print('Book table before creating record')
        self.display_table_content()

        print('Table after creating record:')
        db_insert = f'INSERT INTO books (id, user_id, name, pages, created_at, updated_at) VALUES {args}'
        self.cursor.execute(db_insert)
        self.connection.commit()
        count = self.cursor.rowcount

        self.display_table_content()
        print(count, "Record created successfully in books table")
