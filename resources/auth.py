from flask_restful import Resource
from flask import request
from middleware import create_token, hash_password, strip_token, read_token, check_password
from models.user import User

class Register(Resource):
    def post(self):
        data = request.get_json()
        params = {
            "username": data['username'],
            "name": data['name'],
            "email": data['email'],
            "password": hash_password(data['password'])
        }
        user = User(**params)
        user.create()
        return user.json(), 201
    
class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['email'])
        return user.json(), 201