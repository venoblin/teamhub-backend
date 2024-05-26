from flask import request
from sqlalchemy.orm import joinedload
from models.notification import Notification

def get_all_notifications():
  data = Notification.find_all()
  results = [n.json() for n in data]
  return results

def post_notification():
  data = request.get_json()

  params = {
    'notification': data['notification'],
    'type': data['type'],
    'user_id': data['user_id'],
    'sender_id': data['sender_id'],
    'project_id': data['project_id']
  }
  notification = Notification(**params)
  notification.create()
  return notification.json(), 201

def get_single_notification(id):
  notification = Notification.query.options(
    joinedload(Notification.sender), 
    joinedload(Notification.project)).filter_by(id=id).first()
  return {
    **notification.json(),
    'sender': notification.sender.json(),
    'project': notification.project.json()
  }

def delete_single_notification(id):
  return Notification.delete_by_id(id)

def patch_single_notification(id):
  data = request.get_json()
  notification = Notification.query.options(
    joinedload(Notification.sender), 
    joinedload(Notification.project)).filter_by(id=id).first().update(data)
  return {
    **notification.json(),
    'sender': notification.sender.json(),
    'project': notification.project.json()
  }