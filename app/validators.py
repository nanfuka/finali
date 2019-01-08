# # def validate_input(createdby, location):

# # zif not createdby or createdby.isspace():
# #             return 'please enter the id of the creator of this redflag'
# #         elif not location or location.isspace():
# #             return 'Enter location.'

# from flask import Flask, jsonify, make_response, request
# def validate_data(value):
#     if not value or value.isspace() or len(value)<2 or len(value)>24 or type(value) == int:
#         return jsonify({"status":404, "message":"please enter all items in the right formart"}), 404
# # def validate_data_type(username):
# #     if not type(username) == str:
# #         return 'status must be an String!!'
# def validate_datas(value):
#     if not value or value.isspace() or len(value)<2 or len(value)>24 or type(value) == int:
#         return jsonify({"status":404, "message":"please enter all items in the right formart"}), 404

# def validate_intdata_type(numbers):
#     if not type(numbers) == int:
#         return 'status must be a number!!'

# def validate_keys(value, lst):
#     if value not in lst:
#         return jsonify({"status":404, "message":"All fields must be present"}), 404

# def input_jsonformat(data):
#     if not type(data) == dict:
#         return jsonify({
#             "message":'Data must be in dictionary format',
#             "required format":{"createdby":2,"incidenttype":"jgjjhghhgjh","location":"hjgjhg", "status":"jhgkjh", "image":"hjgjhg", "video":"vhgfghf", "comment":"hjgjhkj"}
#             }), 400

# # def validate_status(status):
# #     if not status=="draft" or status=="resolved":
# #         return "invalid input"
