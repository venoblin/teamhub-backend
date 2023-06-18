from models.db import db
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    todo = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

    def __init__(self, todo):
        self.todo = todo

    def json(self):
        return {
            'id': self.id,
            'todo': self.todo
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self