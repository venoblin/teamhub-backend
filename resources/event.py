from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.event import get_all_events, post_event, get_single_event, delete_single_event

class Events(Resource):
  def get(self):
    return handle_request(request, get_all_events)
  
  def post(self):
    return handle_request(request, post_event)

class SingleEvent(Resource):
  def get(self, id):
    return handle_request(request, lambda: get_single_event(id))
  
  def delete(self, id):
    return handle_request(request, lambda: delete_single_event(id))