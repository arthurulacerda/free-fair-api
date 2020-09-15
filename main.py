from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Fair(Resource):
    def get(self):
        return jsonify({'msg': 'Hello World!'})


api.add_resource(Fair, '/')

if __name__ == '__main__':
    app.run(debug=True)
