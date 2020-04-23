from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class Covid:
    def __init__(self, url):
        self.url = url

    def get(self):
        r = requests.get(self.url)
        return r.json()


class Infections(Resource):
    def __init__(self):
        pass

    def get(self):
        url = "https://covidtracking.com/api/v1/states/current.json"
        cv = Covid(url=url)
        return cv.get()

api.add_resource(Infections, '/covid')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

