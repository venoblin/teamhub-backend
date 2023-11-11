from sqlalchemy.orm import subqueryload
from models.user import User

def get_all_users():
  data = User.find_all()
  results = [u.json() for u in data]
  return results

def get_single_user(id):
  user = User.query.options(subqueryload(User.projects)).filter_by(id=id).first()

  def construct_project(project):
    todos = [t.json() for t in project.todos]
    bugs = [b.json() for b in project.bugs]
    return {**project.json(), 'todos': todos, 'bugs': bugs}
    
  projects = [construct_project(p) for p in user.projects]

  return {**user.json(), 'projects': projects}

def delete_single_user(id):
  return User.delete_by_id(id)