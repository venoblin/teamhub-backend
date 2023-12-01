from models.db import db
from datetime import datetime

class Feed(db.Model):
  __tablename__ = 'feed'
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  event = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
  project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
  project = db.relationship('Project', back_populates='feed')

  def __init__(self, event):
    self.event = event

  def json(self):
    return {
      'event': self.event,
      'time': self.created_at
    }
  
  def create(self):
    db.session.add(self)
    db.session.commit()
    return self