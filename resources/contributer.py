from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.contributer import get_all_contributers

class Contributers(Resource):
  def get(self):
    return handle_request(request, get_all_contributers)
