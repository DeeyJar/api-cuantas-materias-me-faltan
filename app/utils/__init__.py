import os

BASE_DIR_CARRERA = os.path.dirname(os.path.abspath(__file__))

def Response_ok(data):
    return { 
        'statusCode': 200, 
        'message': 'Se encontro el listado de materias.',
        'data' : data
    }


def Response_NotFound(error):
    return { 
        'statusCode': 404, 
        'message': 'No se encontro la carrera solicitada.',
        'messageError': error,
    }