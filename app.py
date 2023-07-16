import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db
from resources.auth import Register, Login, CheckSession
from resources.user import Users, SingleUser
from resources.project import Projects, SingleProject
from resources.todo_bug import Todos, SingleTodo, Bugs, SingleBug

app = Flask(__name__)
DATABASE_URL = os.getenv('DATABASE_URL')
DEV_DATABASE_URL = os.getenv('DEV_DATABASE_URL')
if DATABASE_URL:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace("://", "ql://", 1)
    app.config['SQLALCHEMY_ECHO'] = False 
    app.env = 'production'
else:
    app.debug = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DATABASE_URL
    app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(CheckSession, '/session')

api.add_resource(Users, '/users')
api.add_resource(SingleUser, '/users/<int:id>')

api.add_resource(Projects, '/projects')
api.add_resource(SingleProject, '/projects/<int:id>')

api.add_resource(Todos, '/todos')
api.add_resource(SingleTodo, '/todos/<int:id>')

api.add_resource(Bugs, '/bugs')
api.add_resource(SingleBug, '/bugs/<int:id>')

if __name__ == '__main__':
    app.run()