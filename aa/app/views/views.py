from flask import Flask, jsonify, request, json
from app.controllers.incident_cont import Redflag
from app.models.incident import Incident, incidents


app = Flask(__name__)
redflag = Redflag()


@app.route('/api/v1/')
def index():
    return jsonify({"status": 201, "message": "hi welcome to ireporter"})


@app.route('/api/v1/redflag')
def get_redflags():
    """ Get all redflags """

    return jsonify({"status": 201, 'redflags': redflag.get_allredflags()}), 200


@app.route('/api/v1/redflag', methods=['POST'])
def add_parcels():
    data = request.get_json()

    createdby = data.get('createdby')
    location = data.get('location')
    comment = data.get('comment')
    redflags = data.get('redflags')
    intervention = data.get('intervention')
    status = data.get('status')
    images = data.get('images')
    videos = data.get('videos')
    redflag = Redflag()
    error_message = redflag.validate_input(
        createdby, location, redflags, intervention)
    if error_message:
        return jsonify({"status": 404, 'message': error_message}), 404
    new_incident = redflag.create_redflag(
        data['createdby'],
        data['location'],
        data['comment'],
        data['redflags'],
        data['intervention'],
        data['status'],
        data['images'],
        data['videos'])
    return jsonify({
        "status": 201,
        "message": "Added a new incident", "data": new_incident}), 201


@app.route('/api/v1/redflag/<int:redflag_id>', methods=['GET'])
def get_sepecific_record(redflag_id):
    return redflag.get_a_redflag(redflag_id), 200


@app.route('/api/v1/redflag/<int:redflag_id>', methods=['PUT'])
def edit_location(redflag_id):
    return jsonify({"status": 201, "data": redflag.edit_record(redflag_id)})


@app.route('/api/v1/redflag/<int:redflag_id>', methods=['DELETE'])
def remove_sepecific_record(redflag_id):
    return redflag.delete_record(redflag_id)
