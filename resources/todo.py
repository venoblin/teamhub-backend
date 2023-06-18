from flask_restful import Resource
from flask import request
from models.todo import Todo

class Todos(Resource):
    def get(self):
        data = Todo.find_all()
        results = [t.json() for t in data]
        return results
    
    def post(self):
        data = request.get_json()
        params = {
            'todo': data['todo']
        }
        todo = Todo(**params)
        todo.create()
        return todo.json(), 201
    
class SingleTodo(Resource):
    def get(self, id):
        todo = Todo.find_by_id(id)
        return todo.json()
    
    def delete(self, id):
        project = Todo.delete_by_id(id)
        return project