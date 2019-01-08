import unittest
from app.views.views import app
import json
import datetime

class TestUsers(unittest.TestCase):


    
    def setUp(self):
        self.app = app

        self.test_client = app.test_client()
        self.report = {"createdby":"kljklj",

            "location":"fghfjhg", 
            "status":"draft", 
            "images":"hjhj", 
            "videos":"jjh", 
            "comment":"hjgjhkj",
            "redflags":"kjkjhghgjh",
            "intervention":"jhkjhk"
            }

    def test_index(self):
        response = self.test_client.get('api/v1/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "hi welcome to ireporter")
        self.assertEqual(data['status'], 201)


    def test_create_redflag(self):
        response  = self.test_client.post('/api/v1/redflag', json = self.report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'],"Added a new incident")

    def test_create_red_flag_with_wrong_createdby_field(self):
        report = {"createdb":"kljklj",

                    "location":"fghfjhg", 
                    "status":"draft", 
                    "images":"hjhj", 
                    "videos":"jjh", 
                    "comment":"hjgjhkj",
                    "redflags":"kjkjhghgjh",
                    "intervention":"jhkjhk"
                    }
        response  = self.test_client.post('/api/v1/redflag', json = report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], "please enter the id of the creator of this redflag")

    def test_create_red_flag_with_wrong_locationfield(self):
        report = {"createdby":"kljklj",

            "locatin":"fghfjhg", 
            "status":"draft", 
            "images":"hjhj", 
            "videos":"jjh", 
            "comment":"hjgjhkj",
            "redflags":"kjkjhghgjh",
            "intervention":"jhkjhk"
            }
        response  = self.test_client.post('/api/v1/redflag', json = report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], "Enter location.")

    def test_create_red_flag_with_wrong_redflagfield(self):
        report = {"createdby":"kljklj",

            "location":"fghfjhg", 
            "status":"draft", 
            "images":"hjhj", 
            "videos":"jjh", 
            "comment":"hjgjhkj",
            "redfla":"kjkjhghgjh",
            "intervention":"jhkjhk"
            }
        response  = self.test_client.post('/api/v1/redflag', json = report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], "Enter a redflag.")

    def test_create_red_flag_with_wrong_interventionfield(self):
        report = {"createdby":"kljklj",

            "location":"fghfjhg", 
            "status":"draft", 
            "images":"hjhj", 
            "videos":"jjh", 
            "comment":"hjgjhkj",
            "redflags":"kjkjhghgjh",
            "intervent":"jhkjhk"
            }
        response  = self.test_client.post('/api/v1/redflag', json = report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['message'], "Enter intervantion.")

    def test_get_all_redflags(self):
        response  = self.test_client.get('/api/v1/redflag')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 201)

    def test_get_one_redflag(self):
        response  = self.test_client.get('/api/v1/redflag/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
       


        
    


    # # def test_get_all_redflag(self):

    # #     reports = { 

    # #     "comment": "hgvvgfgghgh",
    # #     "createdby": "hggf",
    # #     "images": "hgvhg",
    # #     "intervantion": "HJJH",
    # #     "location": "jhhjvhg",
    # #     "redflag_id": 2,
    # #     "status": "draft",
    # #     "videos": "hgvg"
    # #     }
    # #     response  = self.test_client.post('/api/v1/redflag', json = self.report)
        

    # #     response = self.test_client.get('api/v1/redflag')
    # #     self.assertEqual(response.status_code, 201)
    # # #     report = { 
          
    # # #         "incidenttype" : 'fire the thief',
    # # #         "location" : 'luweero',
    # # #         "status" : 'draft',
    # # #         "images" : 'thief',
    # # #         "videos": 'theft',
    # # #         "comment" : 'this is serious'  
    # # #         }
    # # # #     report = {
    # # # #         "redflag_id" : 1,
    # # # #         "createdon" : datetime.datetime.now(),
    # # # #         "createdby" : 'Deb',
    # # # #         "intervantion" : 'fire the thief',
    # # # #         "location" : 'luweero',
    # # # #         "status" : 'draft',
    # # # #         "images" : 'thief',
    # # # #         "videos": 'theft',
    # # # #         "comment" : 'this is serious'  
    # # # #     }

    # # # #     response  = self.test_client.post(
    # # # #         '/api/v1/redflag',
    # # # #         content_type='application/json',
    # # # #         data=json.dumps(report)
    # # # #     )

    # # # #     message = json.loads(response.data.decode())
    # # # #     self.assertEqual(message['message'], 'report successfully placed')
    # # # #     self.assertEqual(response.status_code, 201)

    # # # def test_user_signup_without_create_user(self):
    # # #     report = { 
    # # #         "intervantion" : 'fire the thief',
    # # #         "location" : 'luweero',
    # # #         "status" : 'draft',
    # # #         "images" : 'thief',
    # # #         "videos": 'theft',
    # # #         "comment" : 'this is serious'  
    # # #     }

    # # #     response  = self.test_client.post('/api/v1/redflag', json = report)
    # # #     self.assertEqual(response.status_code, 201)

    # #     # message = json.loads(response.data.decode())
    # #     # self.assertEqual(message['message'], 'report successfully placed')
    # #     # self.assertEqual(response.status_code, 201)



    # # # def test_report_without_createuser(self):

    # # #     user1 = {
    # # #         'username': 'deborah',
    # # #         'email': 'deb@gmail.com',
    # # #         'password': 'kanatanata'
    # # #     }

    # # #     response1 = self.test_client.post(
    # # #         'api/v1/signup',
    # # #         content_type='application/json',
    # # #         data=json.dumps(user1)
    # # #     )

    # # #     token = json.loads(response1.data.decode())
    # # #     print(token)

    # #     # response = self.test_client.get(
    # #     #     'api/v1/users',
    # #     #     headers={'Authorization': 'Bearer ' + token['token']},
    # #     #     content_type='application/json'
    # #     # )

    # #     # message = json.loads(response.data.decode())

    #     # self.assertEqual(message['message'], 'welco