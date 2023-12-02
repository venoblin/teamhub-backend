from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.project import get_all_projects, post_project, get_single_project, delete_single_project, patch_single_project

class Projects(Resource):
  def get(self):
    return handle_request(request, get_all_projects)
  
  def post(self):
    return handle_request(request, post_project)
  
class SingleProject(Resource):
  def get(self, id):
    return handle_request(request, lambda: get_single_project(id))
  
  def delete(self, id):
    return handle_request(request, lambda: delete_single_project(id))
    
  def patch(self, id):
    return handle_request(request, lambda: patch_single_project(id))
