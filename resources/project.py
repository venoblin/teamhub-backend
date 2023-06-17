from flask_restful import Resource
from models.project import Project

class Projects(Resource):
    @classmethod
    def get(self):
      data = Project.find_all()
      results = [p.json() for p in data]
      return results
    
    @classmethod
    def post():
      pass