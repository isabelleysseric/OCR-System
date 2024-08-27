import os
from PIL import Image

from src.pdf_handler import (
    convert_pdf_to_images,
    extract_text_from_pdf,
    ocr_from_pdf
)


def test_convert_pdf_to_images():
    """Test de la conversion d'un PDF en une liste d'images."""
    pdf_path = "../data/input/pdf_file.pdf"
    assert os.path.exists(pdf_path), f"Le fichier PDF n'existe pas : {pdf_path}"

    # Vérifiez que la sortie est une liste
    images = convert_pdf_to_images(pdf_path)
    assert isinstance(images, list), "La conversion PDF vers images n'a pas retourné une liste."

    # Vérifiez que la liste contient des objets Image
    assert all(
        isinstance(image, Image.Image) for image in images
    ), "La liste ne contient pas uniquement des objets Image."

    print(f"test_convert_pdf_to_images passé avec succès, nombre d'images : {len(images)}")


def test_ocr_from_pdf():
    """Test de l'OCR sur un PDF et vérification du texte extrait."""
    pdf_path = "../data/input/pdf_file.pdf"
    assert os.path.exists(pdf_path), f"Le fichier PDF n'existe pas : {pdf_path}"

    # Vérifiez que du texte a été extrait
    extracted_text = ocr_from_pdf(pdf_path)
    assert isinstance(extracted_text, str), "L'OCR n'a pas retourné une chaîne de caractères."
    assert extracted_text.strip(), "Aucun texte n'a été extrait du PDF."
    with open("../data/test/test_ocr_from_pdf.txt", 'w', encoding='utf-8') as file:
        file.write(extracted_text)

    print("test_ocr_from_pdf passé avec succès.")


def test_extract_text_from_pdf():
    """Test de l'extraction de texte d'un PDF avec PyMuPDF."""
    pdf_path = "../data/input/pdf_file.pdf"
    assert os.path.exists(pdf_path), f"Le fichier PDF n'existe pas : {pdf_path}"

    # Vérifiez que du texte a été extrait
    extracted_text = extract_text_from_pdf(pdf_path)
    assert isinstance(
        extracted_text, str
    ), "L'extraction de texte n'a pas retourné une chaîne de caractères."
    assert extracted_text.strip(), "Aucun texte n'a été extrait du PDF."
    with open("../data/test/test_extract_text_from_pdf.txt", 'w', encoding='utf-8') as file:
        file.write(extracted_text)

    print("test_extract_text_from_pdf passé avec succès.")



if __name__ == "__main__":
    test_convert_pdf_to_images()
    # test_convert_pdf_to_images passé avec succès, nombre d'images : 1

    test_ocr_from_pdf()
    # test_ocr_from_pdf passé avec succès.

    test_extract_text_from_pdf()
    # test_extract_text_from_pdf passé avec succès.
