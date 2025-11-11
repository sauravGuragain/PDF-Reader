# pdf_reader.py

from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text
    except Exception as e:
        return f'Error reading PDF: {str(e)}'

# TODO: Add more PDF processing logic as needed
