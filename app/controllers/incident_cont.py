from app.models.incident import Incident, incidents
from app.models.users import User

from flask import Flask, jsonify, request, json
from ..db import DatabaseConnection

db = DatabaseConnection()


class Redflag():

    # def __init__(self):


    def create_user(self, *args):

        # self.createdby = args[0]
        # self.redflag = args[1]
        # self.intervention = args[2]
        # # self.incident_type =[self.redflag, self.intervention]
        # self.location = args[3]
        # self.status = args[4]
        # self.images = args[5]
        # self.videos = args[6]
        # self.comment = args[7]
        self.firstname = args[0]
        self.lastname = args[1]
        self.othernames = args[2]
        self.email = args[3]
        self.phoneNumber = args[4]
        self.username = args[5]
        self.isAdmin = args[6]
        self.password = args[7]

        users = User(*args)


            #     query = ("INSERT INTO menu(name, description, price)\
            # VALUES('{}', '{}', '{}')\
            # RETURNING foodId, name, description, price")

        query = "INSERT INTO usersoosi (firstname, lastname, othernames, email, \
                phoneNumber, username, isAdmin, password) \
                VALUES ('{}', '{}', '{}','{}', '{}', '{}','{}', False);".format(self.firstname, self.lastname, self.othernames, self.email, self.phoneNumber, self.username, self.isAdmin, self.password)
        db.cursor.execute(query)
        # newinput_display = self.fetch_ones(self.username)
        newinput_display = users.get_dictionary()
        return newinput_display

    # def validate_input(self, createdby, location,redflag, intervention):
    def validate_input(self, createdby, location, redflag, intervention):

        # if createdby not in lst:
        #     return "Createdby field must be present", 404

        if not createdby or createdby.isspace():
            return 'please enter the id of the creator of this redflag'
        elif not location or location.isspace():
            return 'Enter location.'
        elif not redflag or redflag.isspace():
            return 'Enter a redflag.'
        elif not intervention or intervention.isspace():
            return 'Enter intervantion.'

    # def validate_keys(self, createdby, location, lst):
    #     if createdby not in lst:
    #         return "All fields must be present", 404
    #     elif not location or location.isspace():
    #         return 'Email field can not be left empty.'

    def get_allusers(self):
        query = "SELECT * FROM usersoosi"
        db.cursor.execute(query)
        users = db.cursor.fetchall()
        return users

    def get_a_redflag(self, redflag_id):
        record = [
            record for record in incidents if record[
                'redflag_id'] == redflag_id]

        if record:

            return jsonify({"status": 200, "data": record[0]})

        return jsonify({"message": "the record_id is not available"})

    def login(self, username, password):
        query = "SELECT * FROM usersoosi WHERE username='{}';".format(username)
        db.cursor.execute(query)
        user_details = db.cursor.fetchone() 
        if user_details:
            
            if user_details['password'] == password:
                return user_details
            return {"error":"wrong email credentials"}
        return {"error":"wrong login credentials"}
        # if user_details['email'] == email:
        #     return user_details
        # return {"message":"that person with that id aint here baby"}

        
        # if user_details['password'] == password and user_details['username'] == username:
        #     return {"message":"you have successfully logged in"}
        # return {"error":"enter a right username and password"}

    def fetch_one(self, userid):
        query = "SELECT * FROM usersoosi WHERE userid={};".format(userid)
        db.cursor.execute(query)
        user_details = db.cursor.fetchall()
     
        return user_details

    def fetch_ones(self, username):
        query = "SELECT * FROM usersoosi WHERE username='{}';".format(username)
        db.cursor.execute(query)
        user_details = db.cursor.fetchall()
     
        return user_details
    
    # def fetch_one(self, username):
    #     query = "SELECT * FROM usersoosi WHERE username={};".format(username)
    #     db.cursor.execute(query)
    #     user_details = db.cursor.fetchall()
     
        return user_details
    def edit_record(self, redflag_id):
        data = request.get_json(['location'])
        for redflag in incidents:
            if redflag['redflag_id'] == redflag_id:
                redflag['location'] = data
                return redflag

    def delete_record(self, redflag_id):
        record = [
            redflag for redflag in incidents if redflag[
                'redflag_id'] == redflag_id]

        incidents.remove(record[0])
        return jsonify({
            "status":
            200, "message": "was successfully deleted.", "data": record[0]})
