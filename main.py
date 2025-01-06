from flask import Flask, request, jsonify
# from flask_restful import Api, Resource
import pdfplumber

app = Flask(__name__)
# api = Api(app)

@app.route("/")
def home():
    return "Hello, Woooorld!"

@app.route("/cantidadMaterias")
def cantidadMaterias():
    pdf = pdfplumber.open('565_PlanInformatica2023.pdf')

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

    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)