<h1 align="center">Optical Character Recognition (OCR) System</h1>

![OCR System interface image](data/api/OCR-System.png)

<h2 align="center">    

  <!-- Project Repo -->
  <a href="https://github.com/isabelleysseric/OCR-System">
    <img src="https://img.shields.io/badge/Repo-OCR_System-green?style=for-the-badge&logo={ProductsApiRestProject}&logoColor=white" >
  </a>

  <!-- Wiki Project -->
  <a href="https://github.com/isabelleysseric/OCR-System/wiki">
    <img src="https://img.shields.io/badge/Wiki-OCR_System-green?style=for-the-badge&logo={ProductsApiRestProject}&logoColor=white" >
  </a>
    
  <!-- GitHub -->
  <a href="https://github.com/isabelleysseric/">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" >
  </a><br>
    
  <!-- AI Page -->
  <a href="https://isabelleysseric.ai/">
    <img src="https://img.shields.io/badge/AI-Page-blue?style=for-the-badge&logo={AI-Page}&logoColor=white" >
  </a>
    
  <!-- Portfollio -->
  <a href="https://isabelleysseric.com/Resume.html">
    <img src="https://img.shields.io/badge/Portfollio-bfbfbf?style=for-the-badge&logo={Portfollio}&logoColor=white" >
  </a>
    
  <!-- LinkedIn -->
  <a href="https://www.linkedin.com/in/isabelleysseric/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" >
  </a>
  
  <!-- Docker Hub -->
  <a href="https://hub.docker.com/u/isabelleysseric">
    <img src="https://img.shields.io/badge/Docker_Hub-2496ED?style=for-the-badge&logo={dockerhub}&logoColor=#2496ed" >
  </a>

  <!-- Gazebo Sim -->
  <a href="https://hub.docker.com/u/isabelleysseric">
    <img src="https://img.shields.io/badge/Gazebo_Sim-orange?style=for-the-badge&logo={gazebosim}&logoColor=#2496ed" >
  </a>
  
  <!-- GMAIL -->
  <a href="mailto: isabelleysseric@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" >
  </a>
  
</h2>br/>br/>


## Author
[Isabelle Eysseric](https://github.com/isabelleysseric)
<br/>
<br/>


## Project Description

OCR System is a Python application that allows you to extract text from PDF documents, uploaded images or images captured via a webcam. The application uses the Tesseract OCR library to recognize and extract text from images or PDF pages.


## Features

- **Load PDF**: Loads a PDF file and extracts the text from each page.
- **Load Image**: Loads an image from the file system and extracts the text.
- **Capture Image**: Captures an image via a webcam and extracts the text.
- **Extract Text**: Saves the extracted text to a `.txt` file, including information about the source (PDF, uploaded image, captured image).


## Prerequisites

Before using the application, make sure you have installed the following dependencies:

- Python 3.7+
- Tkinter (included with standard Python)
- OpenCV (`cv2`)
- NumPy
- Pillow (`PIL`)
- Tesseract-OCR
- PyMuPDF (`fitz`)
- PDF2Image
- PyTesseract


### Installing Tesseract-OCR

1. Download and install Tesseract-OCR from [the official website](https://github.com/tesseract-ocr/tesseract).
2. Add Tesseract to your PATH or specify the path to `tesseract.exe` in the Python script.


### Installing Python Dependencies

You can install the required Python dependencies by running:

```bash
pip install -r requirements.txt
```


## Usage

To start the application, run the main script:

```bash
python gui.py
```


### User Interface

* **Load PDF**: Open a PDF file, convert each page to an image, and then extract the text.
* **Load Image**: Load an image from your file system to extract the text.
* **Capture Image**: Use your webcam to capture an image and extract the text.
* **Analyze Image**: Apply preprocessing to improve text recognition.
* **Extract Text**: Extract text from the selected source (PDF, loaded image, or captured image) and save the extracted text to a `.txt` file.


### Saving results

When extracting text, a `.txt` file is generated, including information about the source of the text:

* `captured_image_extracted_text.txt`: Text extracted from an image captured via webcam.
* `loaded_image_extracted_text.txt`: Text extracted from an uploaded image.
* `loaded_pdf_extracted_text.txt`: Text extracted from an uploaded PDF file.


## # OCR System

## Project Description

OCR System is a Python application that allows you to extract text from PDF documents, uploaded images or images captured via a webcam. The application uses the Tesseract OCR library to recognize and extract text from images or PDF pages.

## Features

- **Load PDF**: Loads a PDF file and extracts the text from each page.
- **Load Image**: Loads an image from the file system and extracts the text.
- **Capture Image**: Captures an image via a webcam and extracts the text.
- **Extract Text**: Saves the extracted text to a `.txt` file, including information about the source (PDF, uploaded image, captured image).

## Prerequisites

Before using the application, make sure you have installed the following dependencies:

- Python 3.7+
- Tkinter (included with standard Python)
- OpenCV (`cv2`)
- NumPy
- Pillow (`PIL`)
- Tesseract-OCR
- PyMuPDF (`fitz`)
- PDF2Image
- PyTesseract

### Installing Tesseract-OCR

1. Download and install Tesseract-OCR from [the official website](https://github.com/tesseract-ocr/tesseract).
2. Add Tesseract to your PATH or specify the path to `tesseract.exe` in the Python script.

### Installing Python Dependencies

You can install the required Python dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

To start the application, run the main script:

```bash
python gui.py
```

### User Interface

* **Load PDF**: Open a PDF file, convert each page to an image, and then extract the text.
* **Load Image**: Load an image from your file system to extract the text.
* **Capture Image**: Use your webcam to capture an image and extract the text.
* **Analyze Image**: Apply preprocessing to improve text recognition.
* **Extract Text**: Extract text from the selected source (PDF, loaded image, or captured image) and save the extracted text to a `.txt` file.

### Saving results

When extracting text, a `.txt` file is generated, including information about the source of the text:

* `captured_image_extracted_text.txt`: Text extracted from an image captured via webcam.
* `loaded_image_extracted_text.txt`: Text extracted from an uploaded image.
* `loaded_pdf_extracted_text.txt`: Text extracted from an uploaded PDF file.


## Common issues


### `TesseractNotFoundError`

* Make sure Tesseract-OCR is installed and the path to `tesseract.exe` is set correctly in the Python script.


### No text extraction

* Make sure the uploaded image or PDF contains recognizable text. Try improving the image quality or using a higher resolution.


## Contribution

Contributions are welcome! If you have any ideas for improvement, feel free to submit a pull request or open an issue.


## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isabelleysseric/OCR-System/blob/master/LICENSE) file for more information.


