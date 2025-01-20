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
        
        return data
    

def Open_PDF(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    data = []
    for page in pdf.pages:
        text = page.extract_text()
        # matches = re.findall(r"(\d{4})\s*(.*?)\s*(?:\((.*?)\))?", text)
        # for match in matches:
        patron = r"(\d{4})\s*(.*?)\s*(?:\((.*?)\))?"
        for match in re.finditer(patron, text):
            codigo, asignatura, correlativas = match.groups()
            # codigo = match[0].strip()
            # asignatura = match[1].strip()
            # correlativas = match[2].strip()
            data.append({
                "Código": codigo.strip(),
                "Asignatura": asignatura.strip(),
                "Correlativas": correlativas.strip() if correlativas else None
            })
    return data