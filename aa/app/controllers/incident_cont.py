from app.models.incident import Incident, incidents
from flask import Flask, jsonify, request, json


class Redflag():

    def __init__(self):
        self.redflag_list = []

    def create_redflag(self, *args):

        self.createdby = args[0]
        self.redflag = args[1]
        self.intervention = args[2]
        # self.incident_type =[self.redflag, self.intervention]
        self.location = args[3]
        self.status = args[4]
        self.images = args[5]
        self.videos = args[6]
        self.comment = args[7]

        incident = Incident(*args)

        newinput = incident.get_json()
        incidents.append(incident.get_json())
        return newinput

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

    def get_allredflags(self):
        return incidents

    def get_a_redflag(self, redflag_id):
        record = [
            record for record in incidents if record[
                'redflag_id'] == redflag_id]

        if record:

            return jsonify({"status": 200, "data": record[0]})

        return jsonify({"message": "the record_id is not available"})

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
