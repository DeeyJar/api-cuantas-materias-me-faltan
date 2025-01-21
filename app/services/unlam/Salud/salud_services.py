from flask_restx import Resource
import pdfplumber
from app.utils import BASE_DIR_CARRERA
import re

class UNLAMSalud(Resource):
    def get(self,unlam_carrera):
        pdf_path = BASE_DIR_CARRERA + '\\carrera\\unlam\\salud\\'
        if unlam_carrera == 'enfermeria':
            pdf_path = pdf_path + "15_Enfermeria.pdf"
            data = Open_PDF(pdf_path)
        if unlam_carrera == 'medicina':
            pdf_path = pdf_path + "14_Medicina2023.pdf"
            data = Open_PDF(pdf_path)
        if unlam_carrera == 'nutricion':
            pdf_path = pdf_path + "16_Nutricion.pdf"
            data = Open_PDF(pdf_path)
        if unlam_carrera == 'kinesiologia':
            pdf_path = pdf_path + "17_KinesiologiayFisiatria.pdf"
            data = Open_PDF(pdf_path)
        if unlam_carrera == 'anatomia':
            pdf_path = pdf_path + "33_AnatomiaPatologica.pdf"
            data = Open_PDF(pdf_path)
        
        return data

def Open_PDF(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    data = []
    for pages in pdf.pages:
        text = pages.extract_text()
        lines = text.splitlines()
        current_record = None
        for line in lines:
            match = re.match(r"(\d{4}|\d{5})\s+([A-ZÁÉÍÓÚÑ ]+)\s+([\d\s\-]*)", line)
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

    return data