from flask import request
from sqlalchemy.orm import joinedload
from models.contributor import Contributor
from utils import construct_project

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
  contributor = Contributor.query.options(
    joinedload(Contributor.user), 
    joinedload(Contributor.project)).filter_by(id=id).first()
  return {
    **contributor.json(),
    'user': contributor.user.json(),
    'project': construct_project(contributor.project)
  }

def delete_single_contributor(id):
  return Contributor.delete_by_id(id)

def patch_single_contributor(id):
  data = request.get_json()
  contributor = Contributor.find_by_id(id).update(data)
  return contributor.json()