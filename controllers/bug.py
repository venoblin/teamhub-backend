from flask import request
from models.bug import Bug

def get_all_bugs():
  data = Bug.find_all()
  results = [b.json() for b in data]
  return results

def post_bug():
  data = request.get_json()
  params = {
    'bug': data['bug'],
    'project_id': data['project_id']
  }
  bug = Bug(**params)
  bug.create()
  return bug.json(), 201

def get_single_bug(id):
  bug = Bug.find_by_id(id)
  return bug.json()

def delete_single_bug(id):
  return Bug.delete_by_id(id)

def patch_single_bug(id):
  data = request.get_json()
  bug = Bug.find_by_id(id).update(data)
  return bug.json()