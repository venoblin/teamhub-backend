from flask import request
from models.notification import Notification

def get_all_notifications():
  data = Notification.find_all()
  results = [n.json() for n in data]
  return results

def post_notification():
  data = request.get_json()

  params = {
    'notification': data['notification'],
    'user_id': data['user_id']
  }
  notification = Notification(**params)
  notification.create()
  return notification.json(), 201

def get_single_notification(id):
  notification = Notification.find_by_id(id)
  return notification.json()

def delete_single_notification(id):
  return Notification.delete_by_id(id)