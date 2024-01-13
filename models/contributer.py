from models.db import db
from datetime import datetime

class Contributer(db.Model):
  __tablename__ = 'contributers'
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

  def __init__(self, user_id, project_id):
    self.user_id = user_id
    self.project_id = project_id

  def json(self) {
    return {
      'user_id': self.user_id,
      'project_id': self.project_id
    }
  }

