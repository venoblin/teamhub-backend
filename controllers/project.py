from flask import request
from sqlalchemy.orm import subqueryload
from models.project import Project
from controllers.event import post_event

def get_all_projects():
  data = Project.find_all()
  results = [p.json() for p in data]
  return results

def post_project():
  data = request.get_json()

  if ' ' not in data['name']:
    params = {
    'name': data['name'],
    'git_url': data['git_url'],
    'is_private': data['is_private'],
    'owner_id': data['owner_id'],
    }
    project = Project(**params)

    if not project.find_from_user_by_name(params['name'], params['owner_id']):
      project.create()
      created_project = project.json()
      post_event({
        'event': f'Created project',
        'project_id': created_project['id']
      })
      return get_single_project(created_project['id'])
  
    return 'Name already in use', 500
  else:
    return 'Can\'t have spaces in name'

def get_single_project(id):
  project = Project.query.options(subqueryload(Project.user), subqueryload(Project.todos), subqueryload(Project.bugs), subqueryload(Project.events), subqueryload(Project.contributors)).filter_by(id=id).first()
  todos = [t.json() for t in project.todos]
  bugs = [b.json() for b in project.bugs]
  events = [e.json() for e in project.events]
  contributors = [c.get_user() for c in project.contributors]
  return {
    **project.json(),
    'owner': project.user.json(), 
    'todos': todos, 
    'bugs': bugs,
    'events': events,
    'contributors': contributors
  }

def delete_single_project(id):
  return Project.delete_by_id(id)

def patch_single_project(id):
  data = request.get_json()
  project = Project.find_by_id(id).update(data)
  return project.json()