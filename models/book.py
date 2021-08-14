import psycopg2
from psycopg2 import DatabaseError as Error

class Book:
    def __init__(self):
        self.connection = self.connect_db()
        self.cursor = self.connect_db().cursor()
        self.schema_file = '/Users/mac/week-6-assignment-olawale-kareem/schema.sql'
        self.seeder_file = '/Users/mac/week-6-assignment-olawale-kareem/seeder.sql'

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

    def all(self, id):
        db_query = f'''SELECT * FROM books WHERE user_id = {id};'''
        self.cursor.execute(db_query)
        db_response = self.cursor.fetchall()
        for row in db_response:
            print(row, '\n')
        return db_response

    def get(self, book_id):
        db_query = f'SELECT * FROM books WHERE id = {book_id}'
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

    def update(self, id, *args):
        print('Table before updating record')
        print(self.get(id))
        print('Table after updating record')
        db_insert = f'UPDATE books SET (id, name, pages, created_at, updated_at) = {args} WHERE id = {id}'
        self.cursor.execute(db_insert)
        self.connection.commit()
        count = self.cursor.rowcount
        print(self.get(id))
        print(count, "Record updated successfully in users table")

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

    def close_db_connections(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print('PostgreSQL connection is closed')




if __name__ == '__main__':
    try:
        book = Book()
        print(book.load_schema_file())
        print(book.load_seeder_file())
    except Exception as err:
        print("Sorry! we couldn't connect to the db, load schema and seed the table for operations", err)
    else:
        book.display_table_content()
        # book.all(6)
        # book.get(10)
        # book.create(16, 3, 'Shuffletag', 638, '2021/4/1', '2021/7/27')
        # book.update(1 , 1, 'Purpose', 500, '2019-06-14', '2021-01-28')
        # book.destroy(10)
    finally:
        book.close_db_connections()

