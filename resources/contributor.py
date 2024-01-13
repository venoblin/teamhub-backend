from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.contributor import get_all_contributors

class Contributors(Resource):
  def get(self):
    return handle_request(request, get_all_contributors)