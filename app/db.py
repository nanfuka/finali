import psycopg2
import psycopg2.extras
from pprint import pprint
import os

class Database:
    def __init__(self):
        try:
            if not environ.get('DATABASE_URL'):
                self.connection = psycopg2.connect(
                    "postgres://postgres:test@localhost:5432/ireporter")
            else:
                self.connection = psycopg2.connect(environ.get('DATABASE_URL'))
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(
                cursor_factory=RealDictCursor
            )
            self.create_tables()
            self.create_admin()
        except psycopg2.OperationalError as e:
            print(e, "Database Connection failed")

    def create_tables(self):
        tables = (
            """
                CREATE TABLE IF NOT EXISTS user_table4(
                    ID SERIAL PRIMARY KEY NOT NULL,
                    firstname VARCHAR(20) NOT NULL,
                    lastname VARCHAR(20) NOT NULL,
          
                );
            """
        )
        self.cursor.execute(tables)


# class DatabaseConnection:

#     def __init__(self):

#         if os.getenv('DB_NAME') == 'ireporter':
#             self.db_name = 'ireporter'
#         else:
#             self.db_name = 'ireport'

#         try:
#             self.connection = psycopg2.connect(
#                 dbname=self.db_name, user='postgres', host='localhost', password='test', port=5432
#             )
#             self.connection.autocommit = True
#             self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

#             print('Connected to the database successfully.')
#             print(self.db_name)

#             create_users_table = "CREATE TABLE IF NOT EXISTS usa (userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL, lastname VARCHAR NOT NULL);"

#             self.cursor.execute(create_users_table)
#         except Exception as e:
#             pprint(e)
#             pprint('Failed to connect to the database.')



#     def drop_table(self, table_name):
#         drop = f"DROP TABLE {table_name};"
#         self.cursor.execute(drop)


# if __name__ == '__main__':
#     db_name = DatabaseConnection()



