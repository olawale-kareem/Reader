import sqlite3


class SqlDb:
    def __init__(self):
        self.file = '/Users/mac/week-6-assignment-olawale-kareem/grades.csv'

    def connection(self):
        try:
            sql_conn = sqlite3.connect('gradedb.sqlite', timeout=20)
            cursor = sql_conn.cursor()
            return sql_conn, cursor
        except sqlite3.Error as err:
            print('Error while connecting to sqlite', err)

    def test_connect(self):
        conn,cur = self.connection()
        sqlite_query = 'SELECT sqlite_version();'
        cur.execute(sqlite_query)
        record = cur.fetchall()
        print('SQLite Database Version is: ', record)
        return record

    def csv_separator(self):
        with open(self.file, mode='r') as csv_file:
            sql_file = csv_file.readlines()
        sql_table_header = sql_file[0]
        sql_values = sql_file[1:]
        return sql_table_header, sql_values

    def load_csv(self):
        conn, cur = self.connection()
        sql_table_header, sql_values = self.csv_separator()
        sql_table_query = f'CREATE TABLE grades({sql_table_header});'
        cur.execute(sql_table_query)
        for value in sql_values:
            cur.execute(f'INSERT INTO grades ({sql_table_header}) VALUES ({value})')
            conn.commit()

    def drop_db(self):
        conn, cur = self.connection()
        sql_drop_query = f'DROP TABLE grades'
        cur.execute(sql_drop_query)
        conn.commit()
        print('Records table Successfully deleted')

    def create_record(self, *args):
        conn, cur = self.connection()
        sql_table_header, _ = self.csv_separator()
        sql_create_query = f'INSERT INTO grades ({sql_table_header}) VALUES {args}'
        cur.execute(sql_create_query)
        conn.commit()
        print('Record Successfully Created')
        return 'Record Successfully Created'

    def read_all_records(self):
        conn, cur = self.connection()
        sql_read_query = 'SELECT * FROM grades'
        cur.execute(sql_read_query)
        records = cur.fetchall()
        print('Students records: ')
        for record in records:
            print(record)
        return records




