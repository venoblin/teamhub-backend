from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.user import get_all_users, get_single_user, delete_single_user, get_single_user_by_identifier

class Users(Resource):
  def get(self):
    return get_all_users()
    # return handle_request(request, get_all_users)

class SingleUser(Resource):
  def get(self, id):
    return handle_request(request, lambda: get_single_user(id))
  
  def delete(self, id):
    return handle_request(request, lambda: delete_single_user(id))

class SingleUserByIdentifier(Resource):
  def get(self, identifier):
    return handle_request(request, lambda: get_single_user_by_identifier(identifier))