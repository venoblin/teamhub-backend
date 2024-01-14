from sqlalchemy.orm import subqueryload
from models.user import User

def get_all_users():
  data = User.find_all()
  results = [u.json() for u in data]
  return results

def get_single_user(id):
  user = User.query.options(subqueryload(User.projects), subqueryload(User.contributors)).filter_by(id=id).first()

  def construct_project(project):
    todos = [t.json() for t in project.todos]
    bugs = [b.json() for b in project.bugs]
    events = [e.json() for e in project.events]
    return {
      **project.json(), 'todos': todos, 
      'bugs': bugs, 
      'events': events
    }
    
  projects = [construct_project(p) for p in user.projects]
  contributors = [c.get_project() for c in user.contributors]
  return {
    **user.json(), 
    'projects': projects,
    'contributions': contributors
  }

def get_single_user_by_username(username):
  user = User.find_by_username(username)
  return user.json()

def delete_single_user(id):
  return User.delete_by_id(id)