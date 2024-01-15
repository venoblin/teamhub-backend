from models.db import db
from datetime import datetime

class Notification(db.Model):
  __tablename__ = 'notifications'
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  notification = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now)
  user = db.relationship('User', back_populates='notifications')

  def __init__(self, notification, user_id):
    self.notification = notification
    self.user_id = user_id

  def json(self):
    return {
      'notification': self.notification,
      'time': self.created_at
    }
