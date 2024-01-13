from models.contributer import Contributer

def get_all_contributers():
  data = Contributer.find_all()
  results = [c.json() for c in data]
  return results