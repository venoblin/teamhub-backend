from flask_restful import Resource
from middleware import create_token, hash_password, strip_token, read_token, check_password

class Register(Resource):
    def post(self):
        return 'Registering', 201
    
class Login(Resource):
    def post(self):
        return 'Logining', 201