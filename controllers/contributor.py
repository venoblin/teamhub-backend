from flask import request
from models.contributor import Contributor

def get_all_contributors():
  data = Contributor.find_all()
  results = [c.json() for c in data]
  return results

def post_contributor():
  data = request.get_json()
  params = {
    'user_id': data['user_id'],
    'project_id': data['project_id']
  }
  contributor = Contributor(**params)
  contributor.create()
  return contributor.json(), 201

def get_single_contributor(id):
  contributor = Contributor.find_by_id(id)
  return contributor.json()

def delete_single_bug(id):
  return Contributor.delete_by_id(id)

def patch_single_bug(id):
  data = request.get_json()
  contributor = Contributor.find_by_id(id).update(data)
  return contributor.json()