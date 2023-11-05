def update_self(self, update):
  for key, value in update.items():
    setattr(self, key, value)