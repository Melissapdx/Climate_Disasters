from flask import Flask, request
from flask_restful import Resource, Api,reqparse, abort, fields, marshal_with
from model import store_disasters


app = Flask(__name__)
api = Api(app)

disasters = store_disasters()

resource_fields = {
    'type': fields.String,
    'state': fields.String,
    'year': fields.String,
    'disasterid': fields.String,
}


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

api.add_resource(DisasterIndex, '/')
api.add_resource(DisasterByType, '/type/<string:type>')
api.add_resource(DisasterByYear, '/year/<string:year>')
api.add_resource(DisasterByYearandType, '/yeartype/<string:year>/<string:type>')


if __name__ == '__main__':
    app.run(debug=True)