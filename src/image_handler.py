import numpy as np
import pytesseract

from utils.image_utils import (
    adjust_gamma,
    apply_edge_detection,
    apply_gaussian_blur,
    apply_threshold,
    convert_to_grayscale
)



def process_image(image: np.ndarray, filters: list[str] = None) -> np.ndarray:
    """Traite l'image avant d'appliquer l'OCR."""
    grayscale_image = convert_to_grayscale(image)

    if filters is None:
        filters = []

    for filter_name in filters:
        if filter_name == 'threshold':
            grayscale_image = apply_threshold(grayscale_image)
        elif filter_name == 'blur':
            grayscale_image = apply_gaussian_blur(grayscale_image)
        elif filter_name == 'edges':
            grayscale_image = apply_edge_detection(grayscale_image)
        elif filter_name == 'gamma':
            grayscale_image = adjust_gamma(grayscale_image, gamma=1.5)
        else:
            grayscale_image = grayscale_image

    return grayscale_image

def ocr_from_image(image: np.ndarray) -> str:
    """Applique l'OCR à une image et retourne le texte extrait."""
    return pytesseract.image_to_string(image)
