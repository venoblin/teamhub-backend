from flask_restful import Resource
from flask import request
from middleware import verify_auth
from controllers.user import get_all_users, get_single_user, delete_single_user

class Users(Resource):
  def get(self):
    return verify_auth(request, get_all_users)

class SingleUser(Resource):
  def get(self, id):
    return verify_auth(request, lambda: get_single_user(id))
  
  def delete(self, id):
    return verify_auth(request, lambda: delete_single_user(id))
