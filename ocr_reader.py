import pytesseract
from pdf2image import convert_from_path
import PyPDF2
from PIL import Image
import os

def extract_pdf_text(pdf_path):
    text = ""

    # --- 1. Try normal PDF text extraction ---
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except:
        pass

    # --- 2. OCR for scanned PDFs ---
    pages = convert_from_path(pdf_path, 300)

    for img_page in pages:
        ocr_text = pytesseract.image_to_string(img_page)
        text += ocr_text + "\n"

    return text
