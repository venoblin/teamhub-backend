from flask import request
from models.event import Event

def get_all_events():
  data = Event.find_all()
  results = [e.json() for e in data]
  return results

def post_event(event = None):
  data = None

  if event is not None:
    data = event
  else:
    data = request.get_json()

  params = {
    'event': data['event'],
    'project_id': data['project_id']
  }
  event = Event(**params)
  event.create()
  return event.json(), 201

def get_single_event(id):
  event = Event.find_by_id(id)
  return event.json()

def delete_single_event(id):
  return Event.delete_by_id(id)