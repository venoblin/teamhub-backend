from models.db import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True ,nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    projects = db.relationship('Project', cascade='all', back_populates='user')
    contributors = db.relationship('Contributor', cascade='all', back_populates='user')
    notifications = db.relationship('Notification', cascade='all', back_populates='user', order_by="Notification.created_at")

    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password
    
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'email': self.email
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    @classmethod
    def find_all(self):
        return User.query.all()
    
    @classmethod
    def find_by_id(self, id):
        return db.get_or_404(self, id, description=f'User with id: {id} not found!')
    
    @classmethod
    def delete_by_id(self, id):
        user = self.find_by_id(id)
        db.session.delete(user)
        db.session.commit()
        return f'Successfully deleted user with id: {id}'
    
    @classmethod
    def find_by_email(self, email):
        return db.one_or_404(
            db.select(User).filter_by(email=email), 
            description=f'User with email: {email} not found'
        )
    
    @classmethod
    def find_by_username(self, username):
        return db.one_or_404(
            db.select(User).filter_by(username=username),
            description=f'User with username: {username} not found'
        )