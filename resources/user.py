from flask_restful import Resource

class Users(Resource):
  def get(self):
    pass

class SingleUser(Resource):
  def get(self, id):
    pass
    
