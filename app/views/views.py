from flask import Flask, jsonify, request, json
from app.db import Database
from app.controllers.incident_cont import Redflag
from app.models.incident import Incident, incidents
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity


app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'thisismysecret'
redflag = Redflag()


@app.route('/')
def index():
    return jsonify({"status": 201, "message": "hi welcome to ireporter db"})
@app.route('/api/v1/signup', methods=['POST'])
def register_user():
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othernames = data.get('othernames')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    username = data.get('username')
    isAdmin = data.get('isAdmin')
    password = data.get('password')
    redflag = Redflag()
    error_message = redflag.validate_input(
        firstname, lastname, othernames, email)
    if error_message:
        return jsonify({"status": 404, 'message': error_message}), 404
    new_incident = redflag.create_user(data['firstname'], data['lastname'], data['othernames'], data['email'], data['phoneNumber'], data['username'], data['isAdmin'], data['password'])
    token = create_access_token(username)
    return jsonify({
        "status": 201,
        "message": "Added a new incident", "data": new_incident, "access_token":token}), 201


@app.route('/api/v1/signup')
def get_all_users():
    return jsonify({"users": redflag.get_allusers()})


@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    
    data = redflag.login(username, password)
    return jsonify({"status":201, "message":"you have sucessfully logged in", "data":data})
    # if userdetails:
    #     return jsonify({"status": 201, "message": "you have successfully logged in"})
    # return jsonify({"message":"wrong login credentials"})


@app.route('/api/v1/oneuser/<int:userid>')
@jwt_required
def get_one_user(userid):
    username = get_jwt_identity()
    return jsonify({"status":201, "user": redflag.fetch_one(userid)})

@app.route('/api/v1/oneuser/<username>')
def get_one_users(username):
    return jsonify({"user": redflag.fetch_ones(username)})

# @app.route('/api/v1/redflag')
# def get_redflags():
#     """ Get all redflags """

#     return jsonify({"status": 201, 'redflags': redflag.get_allredflags()}), 200


# @app.route('/api/v1/redflag', methods=['POST'])
# def add_parcels():
#     data = request.get_json()

#     createdby = data.get('createdby')
#     location = data.get('location')
#     comment = data.get('comment')
#     redflags = data.get('redflags')
#     intervention = data.get('intervention')
#     status = data.get('status')
#     images = data.get('images')
#     videos = data.get('videos')
#     redflag = Redflag()
#     error_message = redflag.validate_input(
#         createdby, location, redflags, intervention)
#     if error_message:
#         return jsonify({"status": 404, 'message': error_message}), 404
#     new_incident = redflag.create_redflag(
#         data['createdby'],
#         data['location'],
#         data['comment'],
#         data['redflags'],
#         data['intervention'],
#         data['status'],
#         data['images'],
#         data['videos'])
#     return jsonify({
#         "status": 201,
#         "message": "Added a new incident", "data": new_incident}), 201


# @app.route('/api/v1/redflag/<int:redflag_id>', methods=['GET'])
# def get_sepecific_record(redflag_id):
#     return redflag.get_a_redflag(redflag_id), 200


# @app.route('/api/v1/redflag/<int:redflag_id>', methods=['PUT'])
# def edit_location(redflag_id):
#     return jsonify({"status": 201, "data": redflag.edit_record(redflag_id)})


# @app.route('/api/v1/redflag/<int:redflag_id>', methods=['DELETE'])
# def remove_sepecific_record(redflag_id):
#     return redflag.delete_record(redflag_id)
