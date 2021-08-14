import psycopg2
from psycopg2 import DatabaseError as Error


class User:
    def __init__(self):
        self.connection = self.connect_db()
        self.cursor = self.connect_db().cursor()
        self.schema_file = '/Users/mac/week-6-assignment-olawale-kareem/schema.sql'
        self.seeder_file = '/Users/mac/week-6-assignment-olawale-kareem/seeder.sql'

    def connect_db(self):
        try:
            connection = psycopg2.connect( user='mac', password=None, host='127.0.0.1', port='5432', database='test_script')
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
        db_query = f'SELECT * FROM users'
        self.cursor.execute(db_query)
        db_response = self.cursor.fetchall()
        print(
            f'-------------------------------------------- Table:users ---------------------------------------------\n')
        for row in db_response:
            print(row, '\n')
        return db_response

    def all(self):
        db_query = f'SELECT first_name FROM users'
        self.cursor.execute(db_query)
        db_response = self.cursor.fetchall()
        for row in db_response:
            print(row, '\n')
        return db_response

    def get(self, user_id):
        db_query = f'SELECT * FROM users WHERE id = {user_id}'
        self.cursor.execute(db_query)
        db_response = self.cursor.fetchone()
        return db_response

    def create(self, *args):
        print('User table before creating record')
        self.display_table_content()

        print('Table after creating record:')
        db_insert = f'INSERT INTO users (id, first_name, last_name, created_at, updated_at) VALUES {args}'
        self.cursor.execute(db_insert)
        self.connection.commit()
        count = self.cursor.rowcount

        self.display_table_content()
        print(count, "Record created successfully in users table")

    def update(self, id, *args):
        print('Table before updating record')
        print(self.get(id))
        print('Table after updating record')
        db_insert = f'''UPDATE users SET
        (id, first_name, last_name, created_at, updated_at) = {args} WHERE id = {id}'''
        self.cursor.execute(db_insert)
        self.connection.commit()
        count = self.cursor.rowcount
        print(self.get(id))
        print(count, "Record updated successfully in users table")

    def delete(self, id):
        print('User table before deleting record')
        self.display_table_content()

        print('Table after deleting record:')
        delete_query = f'DELETE FROM users WHERE id = {id}'
        self.cursor.execute(delete_query)
        self.connection.commit()
        count = self.cursor.rowcount

        self.display_table_content()
        print(count, "Record deleted successfully in users table")

    def close_db_connections(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print('PostgreSQL connection is closed')

if __name__ == '__main__':
    try:
        user = User()
        print(user.load_schema_file())
        print(user.load_seeder_file())
    except Exception:
        print("Sorry! we couldn't connect to the db, load schema and seed the table for operations")
    else:
        # user.display_table_content()
        # user.all()
        # print(user.get(10))
        user.create(11, 'Charissa', 'Crighton', '2020/8/13', '2021/2/14')
        # user.update(1,1,'Charissa', 'Crighton', '2020/8/13', '2021/2/14')
        # user.delete(10)
    finally:
        user.close_db_connections()
