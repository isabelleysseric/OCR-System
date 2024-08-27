import cv2
import numpy as np

from utils.image_utils import load_image, save_image
from utils.webcam_utils import load_webcam, read_frame, release_webcam



def capture_an_image_from_webcam(output_directory: str = "output") -> np.ndarray:
    """Capture une image depuis la webcam et l'enregistre dans un répertoire."""
    # Initialise la webcam
    cap = load_webcam()

    while True:
        # Lire une frame de la webcam et l'afficher
        frame = read_frame(cap)
        cv2.imshow("Appuyez sur 's' pour capturer l'image ou 'q' pour quitter", frame)

        # Attendre une touche
        key = cv2.waitKey(1) & 0xFF

        # Capturer et enregistrer l'image
        if key == ord('s'):
            image_path = f"{output_directory}/captured_image.png"
            save_image(frame, image_path)
            print(f"Image capturée et enregistrée sous : {image_path}")
            release_webcam(cap)
            return load_image(image_path)

        # Quitter sans capturer
        elif key == ord('q'):
            print("Capture interrompue par l'utilisateur.")
            break

    # Libérer les ressources et retourner la frame
    release_webcam(cap)
    return frame

def capture_multi_images_from_webcam(output_directory: str = "output", max_images: int = 5) -> list[str]:
    """Capture plusieurs images depuis la webcam et les enregistre dans un répertoire."""
    # Initialisation
    cap = load_webcam()
    image_paths = []
    image_count = 0

    while True:
        # Lire une frame de la webcam et l'afficher
        frame = read_frame(cap)
        cv2.imshow("Appuyez sur 's' pour capturer l'image, 'q' pour quitter", frame)

        # Attendre une touche
        key = cv2.waitKey(1) & 0xFF

        # Capturer et enregistrer l'image
        if key == ord('s'):
            image_count += 1
            image_path = f"{output_directory}/captured_image_{image_count}.png"
            save_image(frame, image_path)
            image_paths.append(image_path)
            print(f"Image capturée et enregistrée sous : {image_path}")

            if image_count >= max_images:
                print("Nombre maximum d'images capturées.")
                break

        # Quitter sans capturer
        elif key == ord('q'):
            print("Capture interrompue par l'utilisateur.")
            break

    print(f"Liste d'images capturées et enregistrées : {image_paths}")

    # Libérer les ressources et retourner le chemin des images
    release_webcam(cap)
    return image_paths