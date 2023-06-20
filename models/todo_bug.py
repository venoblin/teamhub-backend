from models.db import db
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    todo = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    project = db.relationship('Project', back_populates='todos')
    
    def __init__(self, todo, project_id):
        self.todo = todo
        self.project_id = project_id

    def json(self):
        return {
            'id': self.id,
            'todo': self.todo
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(self):
        return Todo.query.all()
    
    @classmethod
    def find_by_id(self, id):
        return db.get_or_404(self, id, description=f'Todo with id: {id} was not found!')
    
    @classmethod
    def delete_by_id(self, id):
        todo = self.find_by_id(id)
        db.session.delete(todo)
        db.session.commit()
        return f'Successfully deleted todo with id: {id}'
    
class Bug(db.Model):
    __tablename__ = 'bugs'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    bug = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    project = db.relationship('Project', back_populates='todos')

    def __init__(self, bug):
        self.bug = bug

    def json(self):
        return {
            'id': self.id,
            'bug': self.bug
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(self):
        return Bug.query.all()
    
    @classmethod
    def find_by_id(self, id):
        return db.get_or_404(self, id, description=f'Todo with id: {id} was not found!')
    
    @classmethod
    def delete_by_id(self, id):
        bug = self.find_by_id(id)
        db.session.delete(bug)
        db.session.commit()
        return f'Successfully deleted todo with id: {id}'