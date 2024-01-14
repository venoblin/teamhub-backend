def update_self(self, update):
  for key, value in update.items():
    setattr(self, key, value)

def contains_email(string):
    return '@' in string and '.com' in string