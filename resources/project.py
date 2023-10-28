from flask_restful import Resource
from flask import request
from sqlalchemy.orm import subqueryload
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
      'owner_id': data['owner_id'],
    }
    project = Project(**params)

    if not project.find_from_user_by_name():
      project.create()
      return project.json(), 201
    
    return 'Name already in use', 500
  
class SingleProject(Resource):
  def get(self, id):
    project = Project.query.options(subqueryload(Project.user), subqueryload(Project.todos), subqueryload(Project.bugs)).filter_by(id=id).first()
    todos = [t.json() for t in project.todos]
    bugs = [b.json() for b in project.bugs]
    return {
      **project.json(),
      'owner': project.user.json(), 
      'todos': todos, 
      'bugs': bugs}
  
  def delete(self, id):
    return Project.delete_by_id(id)
    
  def patch(self, id):
    data = request.get_json()
    project = Project.find_by_id(id).update(data)
    return project.json()
