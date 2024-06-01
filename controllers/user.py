from sqlalchemy.orm import joinedload
from models.user import User
from utils import contains_email, construct_project, construct_notification

def get_all_users():
  data = User.find_all()
  results = [u.json() for u in data]
  return results

def get_single_user(id):
  user = User.query.options(
    joinedload(User.projects), 
    joinedload(User.contributors), 
    joinedload(User.notifications)).filter_by(id=id).first()
  
  projects = [construct_project(p) for p in user.projects]
  contributors = [construct_project(c.project) for c in user.contributors]
  notifications = [construct_notification(n) for n in user.notifications]
  return {
    **user.json(), 
    'projects': projects,
    'contributions': contributors,
    'notifications': notifications
  }

def get_single_user_by_identifier(identifier):
  if contains_email(identifier):
    user = User.find_by_email(identifier)
    return user.json()

  user = User.find_by_username(identifier)
  return user.json()

def delete_single_user(id):
  return User.delete_by_id(id)