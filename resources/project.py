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
      "name": data['name']
    }
    project = Project(**params)
    project.create()
    return project.json(), 201