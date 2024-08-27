import cv2
import os
import numpy as np

from utils.image_utils import load_image
from src.webcam_handler import capture_an_image_from_webcam, capture_multi_images_from_webcam



def test_capture_an_image_from_webcam():
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)
    image = capture_an_image_from_webcam(output_directory=output_directory)
    assert image is not None, "L'image capturée est vide."
    assert isinstance(image, np.ndarray), "L'image capturée n'est pas un tableau NumPy."
    image_path = os.path.join(output_directory, "captured_image.png")
    assert os.path.exists(image_path), f"L'image capturée n'a pas été sauvegardée sous : {image_path}"
    print("test_capture_an_image_from_webcam passé avec succès.")

def test_capture_multi_images_from_webcam():
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)
    max_images = 5
    image_paths = capture_multi_images_from_webcam(output_directory, max_images)

    # Vérifiez que le nombre d'images capturées est inférieur ou égal à max_images
    assert len(
        image_paths
    ) <= max_images, f"Le nombre d'images capturées dépasse le maximum autorisé : {len(image_paths)}"

    # Vérifie que le nombre d'images capturées est supérieur à zéro (si des images ont été capturées)
    if len(image_paths) > 0:
        # Verifie le contenue: chemin et images capturées
        for path in image_paths:
            assert os.path.exists(path), f"L'image n'a pas été sauvegardée sous : {path}"
            image = load_image(path)
            assert isinstance(image, np.ndarray), f"L'image à {path} n'est pas un tableau NumPy."

    print("test_capture_multi_images_from_webcam passé avec succès.")

if __name__ == "__main__":
    test_capture_an_image_from_webcam()
    # Output pour 'q':
    #   Capture interrompue par l'utilisateur.
    #   test_capture_an_image_from_webcam passé avec succès.
    # Output pour 's':
    #   Image capturée et enregistrée sous : output/captured_image.png
    #   test_capture_an_image_from_webcam passé avec succès.


    test_capture_multi_images_from_webcam()
    # Output pour 'q':
    #   Aucune image capturée.
    #   test_capture_multi_images_from_webcam passé avec succès.
    # Output pour 's', 's', 's' et 'q':
    #   Image capturée et enregistrée sous : output/captured_image_1.png
    #   Image capturée et enregistrée sous : output/captured_image_2.png
    #   Image capturée et enregistrée sous : output/captured_image_3.png
    #   Capture interrompue par l'utilisateur après 3 image(s).
    #   Liste d'image capturée et enregistrée : ['output/captured_image_1.png', 'output/captured_image_2.png', 'output/captured_image_3.png']
    #   test_capture_multi_images_from_webcam passé avec succès.

