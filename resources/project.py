from flask_restful import Resource
from flask import request
from models.project import Project

class Projects(Resource):
  def get(self):
    data = Project.find_all()
    results = [p.json() for p in data]
    return results
    
  def post(self):
    data = request.get_json()
    params = {
      'name': data['name'],
      'owner_id': data['owner_id']
    }
    project = Project(**params)
    project.create()
    return project.json(), 201
  
class SingleProject(Resource):
  def get(self, id):
    project = Project.find_by_id(id)
    return project.json()
  
  def delete(self, id):
    project = Project.delete_by_id(id)
    return project

