from flask_restx import Resource
import pdfplumber
from app.utils import BASE_DIR_CARRERA, Response_ok, Response_Error, Response_NotFound
import re

class UNLAMSalud(Resource):
    def get(self,unlam_carrera):
        pdf_path = BASE_DIR_CARRERA + '\\carrera\\unlam\\salud\\'
        if unlam_carrera == 'enfermeria':
            pdf_path = pdf_path + "15_Enfermeria.pdf"
            data = Open_PDF_ENFERMERIA(pdf_path)
        if unlam_carrera == 'medicina': #revisar
            pdf_path = pdf_path + "14_Medicina2023.pdf"
            data = Open_PDF_ANATOMIA(pdf_path)
        if unlam_carrera == 'nutricion':
            pdf_path = pdf_path + "16_Nutricion.pdf"
            data = Open_PDF(pdf_path)
        if unlam_carrera == 'kinesiologia':
            pdf_path = pdf_path + "17_KinesiologiayFisiatria.pdf"
            data = Open_PDF(pdf_path)
        if unlam_carrera == 'anatomia':
            pdf_path = pdf_path + "33_AnatomiaPatologica.pdf"
            data = Open_PDF_ANATOMIA(pdf_path)
        
        return data

def Open_PDF_ENFERMERIA(pdf_path):
    try:
        pdf = pdfplumber.open(pdf_path)
        data = []
        for pages in pdf.pages:
            text = pages.extract_text()
            lines = text.splitlines()
            print(lines)
            current_record = None
            for line in lines:
                match = re.match(r"(\d{4}|\d{5})\s+([A-ZÁÉÍÓÚÑ ]+)\s+([\d{4}\s\-]*)", line)
                if match:
                    if current_record:
                        data.append(current_record)

                    current_record = {
                        "Código": match.group(1),
                        "Asignatura": match.group(2),
                        "Correlativas": match.group(3).strip(),
                    }
                else:
                    if current_record:
                        if re.match(r"^[\d\s\-]+$", line.strip()):
                            current_record["Correlativas"] += f" - {line.strip()}"
            if current_record:
                data.append(current_record)

        return  Response_ok(data)
    except FileNotFoundError:
        return Response_Error("El pdf no se encontro")
    except IndexError:
        return Response_Error("El pdf se encuentra vacio")
    except	Exception as e:
        return Response_Error(e)
    
def Open_PDF(pdf_path):
    try:
        pdf = pdfplumber.open(pdf_path)
        data = []
        for pages in pdf.pages:
            text = pages.extract_text()
            lines = text.splitlines()
            for line in lines:
                match = re.match(r"(\d{4}|\d{5})\s+([A-ZÁÉÍÓÚÑ ]+)(?:\s+(.+))?$", line)
                if match:
                    codigo, asignatura, correlativas = match.groups()
                    if not correlativas:
                        correlativas = "--"
                    else:
                        correlativas = expand_ranges(correlativas)

                    correlativas = correlativas.replace(" y ", " - ")
                    data.append({
                        "Código": codigo,
                        "Asignatura": asignatura,
                        "Correlativas": correlativas
                    })

        return  Response_ok(data)
    except FileNotFoundError:
        return Response_Error("El pdf no se encontro")
    except IndexError:
        return Response_Error("El pdf se encuentra vacio")
    except	Exception as e:
        return Response_Error(e)
    
def Open_PDF_ANATOMIA(pdf_path):
    try:
        pdf = pdfplumber.open(pdf_path)
        data = []
        for pages in pdf.pages:
            text = pages.extract_text_simple()
            text = text.replace('º ','')
            text = text.replace('---','--')
            lines = text.splitlines()
            current_record = None
            for line in lines:
                match = re.match(r"(\d{5})\s+([A-ZÁÉÍÓÚÑ ]+)(?:\s+(.+))?$", line)
                if match:
                    if current_record:
                        data.append(current_record)

                    current_record = {
                        "Código": match.group(1),
                        "Asignatura": match.group(2),
                        "Correlativas": match.group(3).strip(),
                    }
                else:
                    if current_record:
                        if re.match(r"^[\d\s\-]+$", line.strip()):
                            current_record["Correlativas"] += f" - {line.strip()}"

            if current_record:
                data.append(current_record)

        return  Response_ok(data)
    except FileNotFoundError:
        return Response_Error("El pdf no se encontro")
    except IndexError:
        return Response_Error("El pdf se encuentra vacio")
    except	Exception as e:
        return Response_Error(e)


# Función para expandir rangos indicados con "a"
def expand_ranges(correlativas):
    # Buscar rangos en el formato "XXXX a YYYY"
    range_pattern = re.compile(r"(\d{4})\s+a\s+(\d{4})")
    # Reemplazar cada rango con su expansión
    def replace_range(match):
        start, end = map(int, match.groups())
        return " - ".join(map(str, range(start, end + 1)))
    return range_pattern.sub(replace_range, correlativas)
