from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.notification import get_all_notifications, post_notification, get_single_notification, delete_single_notification

class Notifications(Resource):
  def get(self):
    return handle_request(request, get_all_notifications)
  
  def post(self):
    return handle_request(request, post_notification)

class SingleNotification(Resource):
  def get(self, id):
    return handle_request(request, lambda: get_single_notification(id))
  
  def delete(self, id):
    return handle_request(request, lambda: delete_single_notification(id))