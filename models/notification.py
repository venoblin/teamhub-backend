from models.db import db
from datetime import datetime, timezone
from utils import update_self

class Notification(db.Model):
  __tablename__ = 'notifications'
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  notification = db.Column(db.String(255), nullable=False)
  type = db.Column(db.String(80), nullable=False)
  seen = db.Column(db.Boolean, default=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
  created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False, onupdate=datetime.now)
  project = db.relationship('Project', back_populates='notifications')
  user = db.relationship('User', back_populates='notifications')

  def __init__(self, notification, type, user_id, project_id):
    self.notification = notification
    self.type = type
    self.user_id = user_id
    self.seen = False

    if project_id:
      self.project_id = project_id
    else:
      self.project_id = None

  def json(self):
    return {
      'id': self.id,
      'notification': self.notification,
      'type': self.type,
      'seen': self.seen,
      'time': str(self.created_at),
      'user_id': self.user_id
    }
  
  def create(self):
    db.session.add(self)
    db.session.commit()
    return self
  
  def update(self, update):
    update_self(self, update)
    db.session.commit()
    return self
    
  @classmethod
  def find_all(self):
    return Notification.query.all()
  
  @classmethod
  def find_by_id(self, id):
    return db.get_or_404(self, id, description=f'Notification with id: {id} not found!')
  
  @classmethod
  def delete_by_id(self, id):
    notification = self.find_by_id(id)
    db.session.delete(notification)
    db.session.commit()
    return f'Successfully deleted notification with id: {id}'