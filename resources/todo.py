from flask_restful import Resource
from flask import request
from models.todo import Todo

class Todos(Resource):
    def get():
        data = Todo.find_all()
        return data.json()
    
    def post():
        data = request.get_json()
        params = {
            'todo': data['todo']
        }
        todo = Todo.create(**params)
        return todo.json()