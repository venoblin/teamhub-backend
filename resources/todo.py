from flask_restful import Resource
from flask import request
from middleware import verify_auth
from controllers.todo import get_all_todos, post_todo, get_single_todo, delete_single_todo

class Todos(Resource):
    def get(self):
        return verify_auth(request, get_all_todos)
    
    def post(self):
        return verify_auth(request, post_todo)
    
class SingleTodo(Resource):
    def get(self, id):
        return verify_auth(request, lambda: get_single_todo(id))
    
    def delete(self, id):
        return verify_auth(request, lambda: delete_single_todo(id))