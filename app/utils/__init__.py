import os
import pdfplumber
from flask import jsonify, make_response

BASE_DIR_CARRERA = os.path.dirname(os.path.abspath(__file__))

def Response_ok(data):
    response = {
        'statusCode': 200, 
        'message': 'Se encontró el listado de materias.',
        'data': data
    }
    return make_response(jsonify(response), 200)

def Response_Error(error):
    response = { 
        'statusCode': 400, 
        'message': error
    }
    return make_response(jsonify(response), 400)

def Response_NotFound():
    response = { 
        'statusCode': 404, 
        'message': 'No se encontro la carrera solicitada.'
    }
    return make_response(jsonify(response), 404)

def Open_PDF(path, filter):
    try:
        pdf = pdfplumber.open(path)
        table = []
        for i in pdf.pages:
            table.append(i.extract_tables())

        data = []
        for lista in table:
            for sublista in lista:
                for element in sublista:
                    filter_data = [elemento.replace('\n', ' ') for elemento in element 
                                if elemento not in filter]
                    if len(filter_data) > 1:
                        data.append(filter_data)

        return  Response_ok(data)
    except FileNotFoundError:
        return Response_Error("El pdf no se encontro")
    except IndexError:
        return Response_Error("El pdf se encuentra vacio")
    except	Exception as e:
        return Response_Error(e)