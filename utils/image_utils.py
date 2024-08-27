import cv2
import numpy as np



def load_image(img_path: str) -> np.ndarray:
    """Charge une image avec open-cv."""
    image = cv2.imread(img_path)
    if image is None:
        print(f"Erreur : Impossible de charger l'image à partir de {img_path}.")
    return image

def save_image(image: np.ndarray | cv2.VideoCapture, image_path: str = "image.png") -> None:
    """Sauvegarde une image open-cv"""
    return cv2.imwrite(image_path, image)

def convert_to_cv_image(image: np.ndarray) -> np.ndarray:
    """Convertit une image en image open-cv."""
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

def convert_to_np_image(image: np.ndarray) -> np.ndarray:
    """Convertit une image en image open-cv."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """Convertit une image open-cv en niveaux de gris."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_threshold(image: np.ndarray, threshold_value: int = 128) -> np.ndarray:
    """Applique un seuillage binaire à l'image open-cv."""
    _, thresh_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return thresh_image

def apply_gaussian_blur(image: np.ndarray, kernel_size: tuple[int, int] = (5, 5)) -> np.ndarray:
    """Applique un flou gaussien à l'image open-cv."""
    return cv2.GaussianBlur(image, kernel_size, 0)

def apply_edge_detection(image: np.ndarray) -> np.ndarray:
    """Applique un filtre de détection des contours à l'image open-cv."""
    return cv2.Canny(image, 100, 200)

def adjust_gamma(image: np.ndarray, gamma: float = 1.0) -> np.ndarray:
    """Applique une correction gamma à l'image open-cv."""
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** invGamma * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def deskew_image(image: np.ndarray) -> np.ndarray:
    """Détection Automatique et Redressement d'une image open-cv."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    coords = np.column_stack(np.where(gray > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated
