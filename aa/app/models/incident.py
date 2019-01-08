import datetime
incidents = []


class Incident:

    def __init__(self, *args):
        self.createdby = args[0]
        self.location = args[1]
        self.comment = args[2]
        self.redflag = args[3]
        self.intervention = args[4]
        self.status = args[5]
        self.images = args[6]
        self.videos = args[7]

    def get_json(self):

        return{
            "redflag_id": len(incidents) + 1,
            "createdon": datetime.datetime.now(),
            "createdby": self.createdby,
            "incident_type": [{
                "redflag": self.redflag, "intervantion": self.intervention}],
            "location": self.location,
            "status": [{"status": self.status}],
            "images": [{"images": self.images}],
            "videos": [{"videos": self.videos}],
            "comment": self.comment

        }
