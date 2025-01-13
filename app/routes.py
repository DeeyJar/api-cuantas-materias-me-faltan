from flask import Flask
from flask_restful import Api
from app.services.unlam.Ingenieria.unlam_services import UnlamIngenieria

def configure_routes(app: Flask):
    api = Api(app)

    api.add_resource(UnlamIngenieria, '/unlam/<string:unlam_carrera>')