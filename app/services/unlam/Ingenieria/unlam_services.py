from flask_restx import Resource
from app.utils import BASE_DIR_CARRERA, Open_PDF, Response_NotFound

UNLAM_FILTER_ING_INFORMATICA = ('', None,
                        'PRIMER CUATRIMESTRE',
                        'SEGUNDO CUATRIMESTRE',
                        'semanales',
                        'Título Intermedio: Técnico Universitario en Desarrollo de Software',
                        'Para su obtención se requiere tener aprobadas todas las asignaturas de los tres primeros años\ninclusive, niveles I y II de Inglés Transversal',
                        'CONOCIMIENTOS COMUNES REQUERIDOS POR HCS DE LA UNLaM',
                        'Código',
                        'Asignatura',
                        'Correlatividad',
                        'Horas',
                        'Horas\nsemanales')

UNLAM_FILTER_ING_CIVIL = ('', None,'Código','Asignatura','Correlatividad','Horas','Régimen','Cuatrimestral')

UNLAM_FILTER_ING_ARQUITECTURA = ('',None,'Código','Asignatura','Correlatividad','Horas semanales')

UNLAM_FILTER_ING_MECANICA = ('',None,'Código','Asignatura','Correlatividad','Horas semanales','Horas cuatrimestrales',
                            'Total de horas anuales de transversales','384')

UNLAM_FILTER_ING_ELETRONICA = ('',None)

UNLAM_FILTER_ING_INDUSTRIAL = ('',None)

class UNLAMIngenieria(Resource):
    def get(self,unlam_carrera):
        pdf_path = BASE_DIR_CARRERA + '\\carrera\\unlam\\'
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


