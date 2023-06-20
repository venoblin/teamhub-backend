from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload
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
      'git_url': data['git_url'],
      'owner_id': data['owner_id'],
    }
    project = Project(**params)
    project.create()
    return project.json(), 201
  
class SingleProject(Resource):
  def get(self, id):
    project = Project.query.options(joinedload(Project.todos)).filter_by(id=id).first()
    todos = [p.json() for p in project.todos]
    return {**project.json(), 'todos': todos}
  
  def delete(self, id):
    return Project.delete_by_id(id)
    
  def patch(self, id):
    data = request.get_json()
    project = Project.find_by_id(id).update(data)
    return project.json()
