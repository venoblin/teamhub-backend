from flask import request
from models.todo import Todo

def get_all_todos():
  data = Todo.find_all()
  results = [t.json() for t in data]
  return results

def post_todo():
  data = request.get_json()
  params = {
    'todo': data['todo'],
    'project_id': data['project_id']
  }
  todo = Todo(**params)
  todo.create()
  return todo.json(), 201

def get_single_todo(id):
  todo = Todo.find_by_id(id)
  return todo.json()

def delete_single_todo(id):
  return Todo.delete_by_id(id)
