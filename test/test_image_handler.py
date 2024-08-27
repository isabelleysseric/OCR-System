import cv2
import numpy as np

from src.image_handler import ocr_from_image, process_image
from utils.image_utils import load_image, save_image



def test_process_image():
    """Test du traitement d'image avec différents filtres."""
    # Verrifie le chargement de l'image
    image_path = "../data/input/image_file.png"
    image = load_image(image_path)
    assert image is not None, f"L'image n'a pas pu être chargée : {image_path}"

    # Applique différents filtres
    filters = ['threshold', 'blur', 'edges', 'gamma']
    processed_image = process_image(image, filters)
    save_image(processed_image, "../data/test/test_process_image.png")

    # Vérifie que le résultat est une image (np.ndarray) et qu'elle n'est pas vide
    assert isinstance(
        processed_image, np.ndarray
    ), "Le résultat du traitement n'est pas un tableau NumPy."
    assert processed_image.size > 0, "L'image traitée est vide."

    print("test_process_image passé avec succès.")


def test_ocr_from_image():
    """Test de l'OCR sur une image traitée."""
    # Chargez l'image de test
    image_path = "../data/input/image_file.png"
    image = load_image(image_path)
    assert image is not None, f"L'image n'a pas pu être chargée : {image_path}"

    # Traitez l'image avec des filtres avant l'OCR
    filters = ['threshold', 'blur', 'gamma']
    processed_image = process_image(image, filters=filters)
    save_image(processed_image, "../data/test/test_ocr_from_image.png")

    # Appliquez l'OCR et Vérifiez que du texte a été extrait
    extracted_text = ocr_from_image(processed_image)
    assert isinstance(extracted_text, str), "L'OCR n'a pas retourné une chaîne de caractères."
    assert extracted_text.strip(), "Aucun texte n'a été extrait de l'image."
    with open("../data/test/test_ocr_from_image.txt", 'w', encoding='utf-8') as file:
        file.write(extracted_text)

    print("test_ocr_from_image passé avec succès.")



if __name__ == "__main__":
    test_process_image()
    # test_process_image passé avec succès.

    test_ocr_from_image()
    # test_ocr_from_image passé avec succès.
