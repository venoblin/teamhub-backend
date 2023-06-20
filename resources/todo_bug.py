from flask_restful import Resource
from flask import request
from models.todo_bug import Todo, Bug

class Todos(Resource):
    def get(self):
        data = Todo.find_all()
        results = [t.json() for t in data]
        return results
    
    def post(self):
        data = request.get_json()
        params = {
            'todo': data['todo'],
            'project_id': data['project_id']
        }
        todo = Todo(**params)
        todo.create()
        return todo.json(), 201
    
class SingleTodo(Resource):
    def get(self, id):
        todo = Todo.find_by_id(id)
        return todo.json()
    
    def delete(self, id):
        return Todo.delete_by_id(id)
    
class Bugs(Resource):
    def get(self):
        data = Bug.find_all()
        results = [b.json() for b in data]
        return results
    
    def post(self):
        data = request.json()
        params = {
            'bug': data['bug'],
            'project_id': data['project_id']
        }
        bug = Bug(**params)
        bug.create()
        return bug.json(), 201
    
class SingleBug(Resource):
    def get(self, id):
        bug = Bug.find_by_id(id)
        return bug.json()
    
    def delete(self, id):
        return Bug.delete_by_id(id)