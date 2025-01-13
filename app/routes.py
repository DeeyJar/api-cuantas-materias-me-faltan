from flask import Flask
from flask_restx import Api
from app.services.unlam.Ingenieria.unlam_services import UNLAMIngenieria
from app.services.utn.Ingenieria.utn_services import UTNIngenieria
def configure_routes(app: Flask):
    api = Api(app)

    api.add_resource(UNLAMIngenieria, '/api/v1/unlam/<string:unlam_carrera>')
    api.add_resource(UTNIngenieria, '/api/v1/utn/<string:utn_carrera>')