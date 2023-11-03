from flask_restful import Resource
from flask import request
from models.bug import Bug

class Bugs(Resource):
    def get(self):
        data = Bug.find_all()
        results = [b.json() for b in data]
        return results
    
    def post(self):
        data = request.get_json()
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
    
    def patch(self, id):
        data = request.get_json()
        bug = Bug.find_by_id(id).update(data)
        return bug.json()