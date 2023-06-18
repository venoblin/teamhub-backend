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
        todo = Todo.create(**params)
        return todo.json()