from models.db import db
from datetime import datetime, timezone

class Event(db.Model):
  __tablename__ = 'events'
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  event = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False, onupdate=datetime.now())
  project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
  project = db.relationship('Project', back_populates='events')

  def __init__(self, event, project_id):
    self.event = event
    self.project_id = project_id

  def json(self):
    return {
      'id': self.id,
      'event': self.event,
      'time': str(self.created_at),
      'project_id': self.project_id
    }
  
  def create(self):
    db.session.add(self)
    db.session.commit()
    return self
  
  @classmethod
  def find_all(self):
    return Event.query.all()
  
  @classmethod
  def find_by_id(self, id):
    return db.get_or_404(self, id, description=f'Event with id: {id} was not found!')
  
  @classmethod
  def delete_by_id(self, id):
    event = self.find_by_id(id)
    db.session.delete(event)
    db.session.commit()
    return f'Successfully deleted event with id: {id}'