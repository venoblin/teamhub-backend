from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db
from resources.auth import Register, Login, CheckSession
from resources.user import Users, SingleUser
from resources.project import Projects
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/project_manager"
app.config['SQLALCHEMY_ECHO'] = True #should be turned off in prod

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

authRoutePrefix = '/auth'
api.add_resource(Register, f'{authRoutePrefix}/register')
api.add_resource(Login, f'{authRoutePrefix}/login')
api.add_resource(CheckSession, f'{authRoutePrefix}/session')
api.add_resource(Users, '/users')
api.add_resource(SingleUser, '/users/<int:id>')

if __name__ == '__main__':
    app.run()