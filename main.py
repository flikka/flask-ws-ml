import os
import sys
from flask import Flask
from flask_restful import Resource, Api

port = os.environ['FLASK_PORT']
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Python Version': sys.version}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()
