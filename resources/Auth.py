from flask_restful import Resource

class Register(Resource):
    def post(self):
        return 'Registering', 201
    
class Login(Resource):
    def post(self):
        return 'Logining', 201