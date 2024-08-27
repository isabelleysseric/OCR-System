from PIL import Image
from pdf2image import convert_from_path
import pymupdf

from src.image_handler import ocr_from_image



def convert_pdf_to_images(pdf_path: str) -> list[Image]:
    """Convertir un document (pdf) en liste d'images."""
    return convert_from_path(pdf_path)

def ocr_from_pdf(pdf_path: str) -> str:
    """Applique l'OCR à un document (pdf) et retourne le texte extrait."""
    images = convert_pdf_to_images(pdf_path)
    full_text = ""
    for image in images:
        full_text += ocr_from_image(image) + "\n"
    return full_text

def extract_text_from_pdf(file_path: str) -> str:
    """Extraction du texte du document (pdf)."""
    text = ""
    doc = pymupdf.open(file_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = page.get_text()
        text += f"--- Page {page_num + 1} ---\n{page_text}\n\n"
    return text
