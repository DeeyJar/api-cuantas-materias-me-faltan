import os
from flask_restful import Resource
from app.utils import BASE_DIR_CARRERA
import pdfplumber

class UnlamIngenieria(Resource):
    def get(self,unlam_carrera):
        pdf_path = BASE_DIR_CARRERA + '\\carrera\\' + unlam_carrera + '.pdf'
        print(pdf_path)
        pdf = pdfplumber.open(pdf_path)
        table = []
        for i in pdf.pages:
            table.append(i.extract_tables())

        data = []
        for lista in table:
            for sublista in lista:
                for element in sublista:
                    filter_data = [elemento.replace('\n', ' ') for elemento in element 
                                if elemento not in ('', 
                                                None,
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
                                                'Horas\nsemanales',
                                                )]
                    if len(filter_data) > 1:
                        data.append(filter_data)

        return data, 200