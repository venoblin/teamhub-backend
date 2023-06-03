from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.run()

api = Api(app)