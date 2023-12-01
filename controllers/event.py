from flask import request
from models.event import Event

def get_all_events():
  data = Event.find_all()
  results = [e.json() for e in data]
  return results