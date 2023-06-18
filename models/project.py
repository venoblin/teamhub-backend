from models.db import db
from datetime import datetime 

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='projects')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(self):
        return Project.query.all()
    
    @classmethod
    def find_by_id(self, id):
        return db.get_or_404(self, id, description=f'Project with id: {id} not found!')
    
    @classmethod
    def delete_by_id(self, id):
        user = self.find_by_id(id)
        db.session.delete(user)
        db.session.commit()
        return f'Successfully deleted user with id: {id}'