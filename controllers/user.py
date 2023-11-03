from models.user import User

def get_all_users():
  data = User.find_all()
  results = [u.json() for u in data]
  return results