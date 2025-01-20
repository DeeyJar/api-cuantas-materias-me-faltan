from flask_restx import Resource
from app.utils import BASE_DIR_CARRERA, Open_PDF, Response_NotFound
from app.utils.constants import UNLAM_FILTER_ING_INFORMATICA, UNLAM_FILTER_ING_CIVIL, UNLAM_FILTER_ING_ARQUITECTURA, UNLAM_FILTER_ING_MECANICA,UNLAM_FILTER_ING_ELETRONICA,UNLAM_FILTER_ING_INDUSTRIAL

class UNLAMIngenieria(Resource):
    def get(self,unlam_carrera):
        pdf_path = BASE_DIR_CARRERA + '\\carrera\\unlam\\ingenieria\\'
        if unlam_carrera == 'informatica':
            pdf_path = pdf_path + "565_PlanInformatica2023.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ING_INFORMATICA)
        elif unlam_carrera == 'civil':
            pdf_path = pdf_path + "35_PlanCivil.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ING_CIVIL)
        elif unlam_carrera == 'arquitectura':
            pdf_path = pdf_path + "441_PlanArquitectura.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ING_ARQUITECTURA)
        elif unlam_carrera == 'mecanica':
            pdf_path = pdf_path + "488_PlanIngenieraMecnica.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ING_MECANICA)
        elif unlam_carrera == 'eletronica':
            pdf_path = pdf_path + "566_PlanElectronica2023.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ING_ELETRONICA)
        elif unlam_carrera == 'industrial':
            pdf_path = pdf_path + "700_PlanIndustrial2024.pdf"
            data = Open_PDF(pdf_path, UNLAM_FILTER_ING_INDUSTRIAL)
        else:
            data = Response_NotFound()
        
        return data


