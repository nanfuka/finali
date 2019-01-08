def __init__(self):

        if os.getenv('DB_NAME') == 'ireporter':
            self.db_name = 'ireporter'
        else:
            self.db_name = 'ireport'

        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name, user='postgres', host='localhost',
                password='test', port=5432
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully.')
            print(self.db_name)


            create_users_table = "CREATE TABLE IF NOT EXISTS users(\
                userId SERIAL NOT NULL PRIMARY KEY, \
                firstname VARCHAR NOT NULL, \
                lastname VARCHAR NOT NULL, \
                othernames VARCHAR NOT NULL, \
                email VARCHAR NOT NULL, \
                phoneNumber INTEGER NOT NULL, \
                username VARCAHR NOT NULL, \
                isAdmin BOOLEAN NOT NULL, \
                password VARCHAR NOT NULL);"
            self.cursor.execute(create_users_table)
            create_table_incident = "CREATE TABLE IF NOT EXISTS incident(\
                redflag_id SERIAL NOT NULL, \
                createdby INTEGER NOT NULL REFERENCES users(user_id), \
                redflag VARCHAR NOT NULL, \
                intervention VARCHAR NOT NULL, \
                location VARCHAR NOT NULL, \
                status VARCHAR NOT NULL, \
                images blob, \
                videos blob, \
                comment VARCHAR NOT NULL, \
                );"
     
    
from flask import jsonify
import psycopg2
import os

class DatabaseConnection:
	def __init__(self):
		try:
			postgres = "sendit"
			if os.getenv('APP_SETTINGS') == 'testing':
				postgres = "test_db"
			self.connection = psycopg2.connect(database=postgres,
								user="postgres",
								host="localhost",
								password="postgres",
								port="5434")
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()

		except Exception as e:
			print(e)
			print('Failed to connect to db')


	def create_tables(self):

		""" Create all database tables"""

		create_table = "CREATE TABLE IF NOT EXISTS users \
			( user_id SERIAL PRIMARY KEY, username VARCHAR(20), \
			email VARCHAR(100), password VARCHAR(100), admin BOOLEAN NOT NULL);"
		self.cursor.execute(create_table)

		create_table = "CREATE TABLE IF NOT EXISTS parcel_orders \
			( parcel_id SERIAL PRIMARY KEY, weight FLOAT,\
			user_id INTEGER NOT NULL REFERENCES users(user_id), \
			pickup_location VARCHAR(20), destination VARCHAR(20), \
			present_location VARCHAR(20), status VARCHAR(20));"
		self.cursor.execute(create_table)
