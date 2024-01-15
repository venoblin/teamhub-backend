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
  
  def create(self):
        db.session.add(self)
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