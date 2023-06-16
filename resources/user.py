from flask_restful import Resource
from models.user import User

class Users(Resource):
  @classmethod
  def get(self):
    data = User.find_all()
    results = [u.json() for u in data]
    return results

class SingleUser(Resource):
  @classmethod
  def get(self, id):
    data = User.find_by_id(id)
    return data.json()
  
  @classmethod
  def delete(self, id):
    data = User.delete_by_id(id)
    return data
