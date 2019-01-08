import psycopg2
import psycopg2.extras
from pprint import pprint
import os


class DatabaseConnection:
    def __init__(self):

        if os.getenv('DB_NAME') == 'ireporter':
            self.db_name = 'ireporter'
        else:
            self.db_name = 'ireport'

        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name, user='postgres', host='localhost', password='test', port=5432
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully.')
            print(self.db_name)

            create_users_table = "CREATE TABLE IF NOT EXISTS usersoosi (userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL, lastname VARCHAR NOT NULL, othernames VARCHAR NOT NULL,username TEXT NOT NULL, email TEXT NOT NULL, phoneNumber INTEGER NOT NULL, isAdmin BOOLEAN NOT NULL, password TEXT NOT NULL);"

            self.cursor.execute(create_users_table)
        except Exception as e:
            pprint(e)
            pprint('Failed to connect to the database.')

    # def register_user(self, username, email, password):
    #     reg_user = f"INSERT INTO users(username, email, password) VALUES('{username}', '{email}', '{password}');"
    #     pprint(reg_user)
    #     self.cursor.execute(reg_user)
    
    # def check_username(self, username):
    #     query = f"SELECT * FROM users WHERE username='{username}';"
    #     pprint(query)
    #     self.cursor.execute(query)
    #     user = self.cursor.fetchone()
    #     return user
    
    # def check_email(self, email):
    #     query = f"SELECT * FROM users WHERE email='{email}';"
    #     pprint(query)
    #     self.cursor.execute(query)
    #     user = self.cursor.fetchone()
    #     return user

    # def login(self, username):
    #     query = f"SELECT * FROM users WHERE username='{username}';"
    #     pprint(query)
    #     self.cursor.execute(query)
    #     user = self.cursor.fetchone()
    #     pprint(user)
    #     return user

    def drop_table(self, table_name):
        drop = f"DROP TABLE {table_name};"
        self.cursor.execute(drop)


if __name__ == '__main__':
    db_name = DatabaseConnection()



# # import psycopg2
# # import psycopg2.extras
# # from pprint import pprint
# # import os


# # from flask import jsonify
# # import psycopg2
# # import os


# # class DatabaseConnection:
# #     def __init__(self):

# #         if os.getenv('DB_NAME') == 'ireporter':
# #             self.db_name = 'ireporter'
# #         else:
# #             self.db_name = 'ireport'

# #         try:
# #             self.connection = psycopg2.connect(
# #                 dbname=self.db_name, user='postgres', host='localhost', password='test', port=5432
# #             )
      
# #             self.connection.autocommit = True
# #             self.cursor = self.connection.cursor()

# #         except Exception as e:
# #             print(e)
# #             print('Failed to connect to db')

# #     def create_tables(self):
# #         """ Create all database tables"""

# #         create_usersi_table = "CREATE TABLE IF NOT EXISTS usersi(\
# #                 userId SERIAL NOT NULL PRIMARY KEY, \
# #                 firstname VARCHAR NOT NULL, \
# #                 lastname VARCHAR NOT NULL, \
# #                 othernames VARCHAR NOT NULL, \
# #                 email VARCHAR NOT NULL, \
# #                 phoneNumber INTEGER NOT NULL, \
# #                 username VARCAHR NOT NULL, \
# #                 isAdmin BOOLEAN NOT NULL, \
# #                 password VARCHAR NOT NULL);"
# #         self.cursor.execute(create_users_table)
#         # create_table_incident = "CREATE TABLE IF NOT EXISTS incident(\
#         #         redflag_id SERIAL NOT NULL, \
#         #         createdby INTEGER NOT NULL REFERENCES users(user_id), \
#         #         redflag VARCHAR NOT NULL, \
#         #         intervention VARCHAR NOT NULL, \
#         #         location VARCHAR NOT NULL, \
#         #         status VARCHAR NOT NULL, \
#         #         images blob, \
#         #         videos blob, \
#         #         comment VARCHAR NOT NULL, \
#         #         );"

#     # def add_user(self, username, email, password):
#     #     query = "INSERT INTO users (username, email, password, admin) VALUES\
# 	# 		('{}', '{}', '{}', False);".format(username, email, password)
#     #     self.cursor.execute(query)

#     # def get_user(self, column, value):
#     #     query = "SELECT * FROM users WHERE {} = '{}';".format(column, value)
#     #     self.cursor.execute(query)
#     #     user = self.cursor.fetchone()
#     #     return user



#     # def auto_admin(self):
#     #     query = "UPDATE users SET admin = True WHERE user_id < 2;"
#     #     self.cursor.execute(query)

#     # def place_order(self, user_id, weight, pickup_location, present_location, destination):
#     #     query = "INSERT INTO parcel_orders (user_id, weight, pickup_location, \
# 	# 		present_location, destination, status)\
# 	# 		VALUES ('{}', '{}', '{}','{}', '{}', 'New');\
# 	# 		".format(user_id, weight, pickup_location, present_location, destination)
#     #     self.cursor.execute(query)

#     # def drop_tables(self):
#     #     query = "DROP TABLE parcel_orders;DROP TABLE users; "
#     #     self.cursor.execute(query)
#     #     return "Droped"

#     # def get_orders(self):
#     #     query = "SELECT * FROM parcel_orders;"
#     #     self.cursor.execute(query)
#     #     orders = self.cursor.fetchall()
#     #     return orders

#     # def get_user_orders(self, id):
#     #     query = "SELECT * FROM parcel_orders where user_id = {};".format(id)
#     #     self.cursor.execute(query)
#     #     orders = self.cursor.fetchall()
#     #     return orders

#     # def get_user_id(self, id):
#     #     query = "SELECT user_id FROM parcel_orders WHERE parcel_id = '{}';".format(
#     #         id)
#     #     self.cursor.execute(query)
#     #     user_id = self.cursor.fetchone()[0]
#     #     return user_id

#     # def update_destination(self, order_id, destination):
#     #     query = "UPDATE parcel_orders SET destination = '{}' WHERE parcel_id = '{}';\
# 	# 	".format(destination, order_id)
#     #     self.cursor.execute(query)

#     # def update_status(self, order_id, status):
#     #     query = "UPDATE parcel_orders SET status = '{}' WHERE parcel_id = '{}';\
# 	# 	".format(status, order_id)
#     #     self.cursor.execute(query)

#     # def update_presentLocation(self, order_id, location):
#     #     query = "UPDATE parcel_orders SET present_location = '{}' WHERE parcel_id = '{}';\
# 	# 	".format(location, order_id)
#     #     self.cursor.execute(query)

#     # def get_an_order(self, column, value):
#     #     query = "SELECT * FROM parcel_orders WHERE {} = '{}'".format(
#     #         column, value)
#     #     self.cursor.execute(query)
#     #     parcel = self.cursor.fetchone()
#     #     return parcel

#     # def validate_data(self, value, lst):
#     #     if value not in lst:
#     #         return jsonify({'message': '{} field must be present'.format(value)}), 400

#     # def get_item_from_parcels(self, item, value):
#     #     query = "SELECT {} FROM parcel_orders WHERE parcel_id = '{}'".format(
#     #         item, value)
#     #     self.cursor.execute(query)
#     #     item = self.cursor.fetchone()
#     #     return item

#     # def get_created_parcel(self):
#     #     query = "SELECT * from parcel_orders ORDER BY parcel_id DESC LIMIT 1"
#     #     self.cursor.execute(query)
#     #     item = self.cursor.fetchone()
#     #     return item

# # if __name__ == '__main__':
# #     app.run(debug=True) 

# # if __name__ == '__main__':
# #     db_name = DatabaseConnection()

# import psycopg2
# import psycopg2.extras
# from pprint import pprint
# import os


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
#             create_users_table = "CREATE TABLE IF NOT EXISTS userso (userId SERIAL NOT NULL PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL);"


#             # create_users_table =  "CREATE TABLE IF NOT EXISTS usersi(userId SERIAL NOT NULL PRIMARY KEY, firstname VARCHAR NOT NULL)"
#                 # lastname VARCHAR NOT NULL, \
#                 # othernames VARCHAR NOT NULL, \
#                 # email VARCHAR NOT NULL, \
#                 # phoneNumber INTEGER NOT NULL, \
#                 # username VARCAHR NOT NULL, \
#                 # isAdmin BOOLEAN NOT NULL, \
#                 # password VARCHAR NOT NULL);"
#             self.cursor.execute(create_users_table)
#         except Exception as e:
#             pprint(e)
#             pprint('Failed to connect to the database.')

# #     def register_user(self, username, email, password):
# #         reg_user = f"INSERT INTO users(username, email, password) VALUES('{username}', '{email}', '{password}');"
# #         pprint(reg_user)
# #         self.cursor.execute(reg_user)
    
# #     def check_username(self, username):
# #         query = f"SELECT * FROM users WHERE username='{username}';"
# #         pprint(query)
# #         self.cursor.execute(query)
# #         user = self.cursor.fetchone()
# #         return user
    
# #     def check_email(self, email):
# #         query = f"SELECT * FROM users WHERE email='{email}';"
# #         pprint(query)
# #         self.cursor.execute(query)
# #         user = self.cursor.fetchone()
# #         return user

# #     def login(self, username):
# #         query = f"SELECT * FROM users WHERE username='{username}';"
# #         pprint(query)
# #         self.cursor.execute(query)
# #         user = self.cursor.fetchone()
# #         pprint(user)
# #         return user

# #     def drop_table(self, table_name):
# #         drop = f"DROP TABLE {table_name};"
# #         self.cursor.execute(drop)


# # if __name__ == '__main__':
# #     db_name = DatabaseConnection()
