from flask import Flask
from flask_restful import Api
from resources.Auth import Register, Login

app = Flask(__name__)

api = Api(app)

authRoutePrefix = '/auth'
api.add_resource(Register, f'{authRoutePrefix}/register')
api.add_resource(Login, f'{authRoutePrefix}/login')

if __name__ == '__main__':
    app.run()