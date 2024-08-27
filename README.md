# OCR System

## Description du projet

OCR System est une application Python qui permet d'extraire du texte à partir de documents PDF, d'images chargées ou d'images capturées via une webcam. L'application utilise la bibliothèque Tesseract OCR pour reconnaître et extraire du texte à partir d'images ou de pages PDF.

## Fonctionnalités

- **Charger un PDF** : Charge un fichier PDF et extrait le texte de chaque page.
- **Charger une Image** : Charge une image à partir du système de fichiers et extrait le texte.
- **Capturer une Image** : Capture une image via une webcam et extrait le texte.
- **Extraire le texte** : Sauvegarde le texte extrait dans un fichier `.txt`, incluant des informations sur la source (PDF, image chargée, image capturée).

## Prérequis

Avant d'utiliser l'application, assurez-vous d'avoir installé les dépendances suivantes :

- Python 3.7+
- Tkinter (inclus avec Python standard)
- OpenCV (`cv2`)
- NumPy
- Pillow (`PIL`)
- Tesseract-OCR
- PyMuPDF (`fitz`)
- PDF2Image
- PyTesseract

### Installation de Tesseract-OCR

1. Téléchargez et installez Tesseract-OCR depuis [le site officiel](https://github.com/tesseract-ocr/tesseract).
2. Ajoutez Tesseract à votre PATH ou spécifiez le chemin vers `tesseract.exe` dans le script Python.

### Installation des dépendances Python

Vous pouvez installer les dépendances Python nécessaires en exécutant :

```bash
pip install -r requirements.txt
```

## Utilisation

Pour démarrer l'application, exécutez le script principal :

```bash
python gui.py
```

### Interface utilisateur

* **Charger un PDF** : Ouvrez un fichier PDF, convertissez chaque page en image, puis extrayez le texte.
* **Charger une Image** : Chargez une image depuis votre système de fichiers pour en extraire le texte.
* **Capturer une Image** : Utilisez votre webcam pour capturer une image et extraire le texte.
* **Analyser l'Image** : Appliquez un prétraitement pour améliorer la reconnaissance de texte.
* **Extraire le Texte** : Extrait le texte de la source sélectionnée (PDF, image chargée ou image capturée) et enregistre le texte extrait dans un fichier `.txt`.

### Sauvegarde des résultats

Lors de l'extraction de texte, un fichier `.txt` est généré, incluant des informations sur la source du texte :

* `captured_image_extracted_text.txt` : Texte extrait d'une image capturée via webcam.
* `loaded_image_extracted_text.txt` : Texte extrait d'une image chargée.
* `loaded_pdf_extracted_text.txt` : Texte extrait d'un fichier PDF chargé.

## Problèmes courants

### Erreur `TesseractNotFoundError`

* Assurez-vous que Tesseract-OCR est installé et que le chemin vers `tesseract.exe` est correctement configuré dans le script Python.

### Aucune extraction de texte

* Vérifiez que l'image ou le PDF chargé contient bien du texte reconnaissable. Essayez d'améliorer la qualité de l'image ou d'utiliser une résolution plus élevée.

## Contribution

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration, n'hésitez pas à soumettre une pull request ou à ouvrir une issue.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE]() pour plus d'informations.

