from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db
from resources.Auth import Register, Login

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

if __name__ == '__main__':
    app.run()