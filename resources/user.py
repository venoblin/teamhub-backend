from flask_restful import Resource
from controllers.user import get_all_users, get_single_user

class Users(Resource):
  def get(self):
    return get_all_users()

class SingleUser(Resource):
  def get(self, id):
    return get_single_user(id)
    
