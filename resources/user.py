from flask_restful import Resource
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import subqueryload
from models.user import User

class Users(Resource):
  def get(self):
    pass

class SingleUser(Resource):
  def get(self, id):
    user = User.query.options(subqueryload(User.projects)).filter_by(id=id).first()

    def construct_project(project):
      todos = [t.json() for t in project.todos]
      bugs = [b.json() for b in project.bugs]
      return {**project.json(), 'todos': todos, 'bugs': bugs}
      
    projects = [construct_project(p) for p in user.projects]

    return {**user.json(), 'projects': projects}
    
