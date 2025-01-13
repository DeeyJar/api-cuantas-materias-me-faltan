from flask_restx import Resource
from app.utils import BASE_DIR_CARRERA
import pdfplumber

class UTNIngenieria(Resource):
    def get(self,utn_carrera):
        pdf_path = BASE_DIR_CARRERA + '\\carrera\\utn\\' + utn_carrera + '.pdf'
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
                                                'I',
                                                'II',
                                                'III',
                                                'IV',
                                                'V',
                                                "Nivel",
                                                "Nº",
                                                "Asignatura",
                                                "Para cursar y rendir",
                                                "Cursadas",
                                                "Aprobadas"
                                                )]
                    if len(filter_data) > 1:
                        data.append(filter_data)

        return data, 200