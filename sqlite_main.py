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

    def read_records_by_SSN(self, SSN):
        conn, cur = self.connection()
        sql_read_query = f"SELECT * FROM grades WHERE SSN = '{SSN}'"
        cur.execute(sql_read_query)
        records = cur.fetchone()
        print(f'Student record: {SSN}')
        print(records)
        return records

    def update_record(self, id, *args):
        conn, cur = self.connection()
        db_insert = f'''UPDATE grades SET
        ( SSN,Test1,Test2,Test3,Test4,Final,Grade) = {args} WHERE SSN = {id}'''
        cur.execute(db_insert)
        conn.commit()
        print("Record updated successfully in users table")
        return "Record updated successfully in users table"

    def final_50_and_above(self):
        conn, cur = self.connection()
        sql_read_query = f"SELECT * FROM grades WHERE Final >= 50"
        cur.execute(sql_read_query)
        records = cur.fetchall()
        print(f'Student records 50 and above:')
        for record in records:
            print(record)
        return records

    def final_50_below(self):
        conn, cur = self.connection()
        sql_read_query = f"SELECT * FROM grades WHERE Final < 50"
        cur.execute(sql_read_query)
        records = cur.fetchall()
        print(f'Student records below 50:')
        for record in records:
            print(record)
        return records




