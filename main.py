from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "tim": {"age": 12, "gender": "Male"},
    "tuwi": {"age": 234, "gender": "Female"},
         }

class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    def post(self):
        return {"data": "posted"}

api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)