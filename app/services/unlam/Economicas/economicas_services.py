from flask_restx import Resource
from app.utils import BASE_DIR_CARRERA, Open_PDF, Response_NotFound

UNLAM_FILTER_ECO_CONTADOR_PUBLICO = ('')
UNLAM_FILTER_ECO_ADMINISTRACION = ('')
UNLAM_FILTER_ECO_COMERCIO_INTERNACIONAL = ('')
UNLAM_FILTER_ECO_ECONOMIA = ('')

class UNLAMEconomicas(Resource):
    def get(self,unlam_carrera):
        pdf_path = BASE_DIR_CARRERA + '\\carrera\\unlam\\economicas\\'
        if unlam_carrera == 'contadorPublico':
            pdf_path = pdf_path + "61_CONTADORPUBLICO.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ECO_CONTADOR_PUBLICO)
        elif unlam_carrera == 'administracion':
            pdf_path = pdf_path + "114_LICENCIATURAENADMINISTRACION.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ECO_ADMINISTRACION)
        elif unlam_carrera == 'comercioInternacional':
            pdf_path = pdf_path + "112_LICENCIATURAENCOMERCIOINTERNACIONAL.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ECO_COMERCIO_INTERNACIONAL)
        elif unlam_carrera == 'economia':
            pdf_path = pdf_path + "113_PlandeestudioECONOMIA.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ECO_ECONOMIA)
        else:
            data = Response_NotFound()
        
        return data


