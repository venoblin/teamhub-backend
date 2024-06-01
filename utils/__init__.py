def update_self(self, update):
  for key, value in update.items():
    setattr(self, key, value)

def contains_email(string):
    return '@' in string and '.com' in string

def construct_project(project):
  todos = [t.json() for t in project.todos]
  bugs = [b.json() for b in project.bugs]
  events = [e.json() for e in project.events]
  contributors = [c.json() for c in project.contributors]
  return {
    **project.json(),
    'owner': project.user.json(), 
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