from flask import Flask
from flask_restx import Api
from app.services.unlam.Ingenieria.ingenieria_services import UNLAMIngenieria
from app.services.unlam.Economicas.economicas_services import UNLAMEconomicas
from app.services.unlam.Salud.salud_services import UNLAMSalud
from app.services.utn.Ingenieria.utn_services import UTNIngenieria
def configure_routes(app: Flask):
    api = Api(app)

    api.add_resource(UNLAMIngenieria, '/api/v1/unlam/ingenieria/<string:unlam_carrera>')
    api.add_resource(UNLAMEconomicas, '/api/v1/unlam/economicas/<string:unlam_carrera>')
    api.add_resource(UNLAMSalud, '/api/v1/unlam/salud/<string:unlam_carrera>')
    api.add_resource(UTNIngenieria, '/api/v1/utn/<string:utn_carrera>')