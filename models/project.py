from models.db import db
from datetime import datetime 

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    @classmethod
    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
    @classmethod
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self