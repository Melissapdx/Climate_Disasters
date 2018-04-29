from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api, fields, marshal_with
from model import store_disasters
import os

# https://stackoverflow.com/questions/44578881/flask-404-url-not-found?noredirect=1&lq=1
static_folder = os.path.join(os.pardir, 'static')
app = Flask(__name__, static_folder=static_folder, static_url_path='/static')
api = Api(app)

disasters = store_disasters()

resource_fields = {
    'type': fields.String,
    'state': fields.String,
    'year': fields.String,
    'disasterid': fields.String,
}


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


class APIIndex(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return [
            {'disasters': '/api/v1/disasters'}
            {'disasters_by_type': '/api/v1/disasters/type/<string:type>'},
            {'disasters_by_year': '/api/v1/disasters/year/<string:year>'},
            {'disasters_by_year_and_type': '/api/v1/disasters/yeartype/<string:year>/<string:type>'}
        ]


class DisasterIndex(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return disasters

class DisasterByType(Resource):
    @marshal_with(resource_fields)
    def get(self, type):
        # Filter the list of disasters by type: Type.
        disasters_of_type = [x for x in disasters if x.type == type]
        return disasters_of_type


class DisasterByYear(Resource):
    @marshal_with(resource_fields)
    def get(self, year):
        # Filter the list of disasters by type: Year.
        disasters_by_year = [x for x in disasters if x.year == year]
        return disasters_by_year


class DisasterByYearandType(Resource):
    @marshal_with(resource_fields)
    def get(self, year,type):
        # Filter by year and type of disasters
        disasters_by_type_year = [y for y in disasters if y.type == type and y.year == year]
        return disasters_by_type_year


# api.add_resource(DisasterIndex, '/api/v1/')
api.add_resource(DisasterIndex, '/api/v1/disasters')
api.add_resource(DisasterByType, '/api/v1/disasters/type/<string:type>')
api.add_resource(DisasterByYear, '/api/v1/disasters/year/<string:year>')
api.add_resource(DisasterByYearandType, '/api/v1/disasters/yeartype/<string:year>/<string:type>')


if __name__ == '__main__':
    app.run(debug=True)