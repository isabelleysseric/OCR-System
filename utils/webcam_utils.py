import cv2



def load_webcam() -> cv2.VideoCapture:
    """Initialiser la webcam."""
    # Par défaut, la webcam est à l'index 0
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erreur : Impossible d'accéder à la webcam.")
    return cap

def release_webcam(cap: cv2.VideoCapture) -> None:
    """Libérer la capture et fermer les fenêtres."""
    cap.release()
    cv2.destroyAllWindows()

def read_frame(cap: cv2.VideoCapture) -> cv2.VideoCapture:
    """Lire une frame de la webcam."""
    ret, frame = cap.read()
    if not ret:
        print("Erreur : Impossible de lire le flux de la webcam.")
    return frame
