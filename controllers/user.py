from sqlalchemy.orm import joinedload
from models.user import User
from models.notification import Notification
from utils import contains_email

def get_all_users():
  data = User.find_all()
  results = [u.json() for u in data]
  return results

def get_single_user(id):
  user = User.query.options(
    joinedload(User.projects), 
    joinedload(User.contributors), 
    joinedload(User.notifications)).filter_by(id=id).first()

  def construct_project(project):
    todos = [t.json() for t in project.todos]
    bugs = [b.json() for b in project.bugs]
    events = [e.json() for e in project.events]
    contributors = [c.json() for c in project.contributors]
    return {
      **project.json(), 
      'todos': todos, 
      'bugs': bugs, 
      'events': events,
      'contributors': contributors
    }
  
  def construct_notification(notification):
    return {
      **notification.json(),
      'sender': notification.sender.json(),
      'project': notification.project.json()
    }
    
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