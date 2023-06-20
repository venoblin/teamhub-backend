from flask_restful import Resource
from sqlalchemy.orm import joinedload
from models.user import User

class Users(Resource):
  def get(self):
    data = User.find_all()
    results = [u.json() for u in data]
    return results

class SingleUser(Resource):
  def get(self, id):
    user = User.query.options(joinedload(User.projects)).filter_by(id=id).first()
    projects = [p.json() for p in user.projects]
    return {**user.json(), 'projects': projects}
  
  def delete(self, id):
    return User.delete_by_id(id)
    
