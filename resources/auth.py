from flask_restful import Resource
from controllers.auth import register_user, login_user, check_session

class Register(Resource):
    def post(self):
        return register_user()
    
class Login(Resource):
    def post(self):
        return login_user()
    
class CheckSession(Resource):
    def post(self):
        return check_session()