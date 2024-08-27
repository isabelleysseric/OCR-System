import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

from src.image_handler import ocr_from_image, process_image
from src.pdf_handler import convert_pdf_to_images, extract_text_from_pdf
from utils.text_utils import save_text
from utils.webcam_utils import load_webcam, read_frame, release_webcam
from utils.image_utils import (
    convert_to_cv_image, convert_to_np_image, convert_to_grayscale,
    load_image, save_image
)



class OCRApp:
    def __init__(self, root):
        self.source_type = None
        self.cap = None
        self.capture_button = None
        self.capture_frame = None
        self.quit_button = None
        self.file_path = None
        self.capture_command = None
        self.status_label = None
        # self.progress_duration = None
        self.progress = None
        self.text_frame = None
        self.text_output = None

        self.root = root
        self.root.title("OCR et Reconnaissance de Formes")
        self.root.geometry("800x600")
        self.root.geometry("1000x800")

        # Définition des couleurs
        light_gray = "#D3D3D3"  # Gris clair pour le fond général
        medium_gray = "#939393"  # Gris moyen pour le fond des boutons
        dark_gray = "#545454"  # Gris foncé pour l'état actif des boutons
        black = "#000000"  # Noir pour le texte

        self.bg_color = light_gray
        self.fg_color = black

        self.root.configure(bg=self.bg_color)

        self.image = None
        self.processed_image = None
        self.ocr_language = "en"  # Langue par défaut pour l'OCR

        # Configurer les styles pour les boutons ttk
        style = ttk.Style()
        style.configure(
            "BW.TLabel",
            background=medium_gray,
            foreground="black",
            font=("Helvetica", 10, "bold"),
            borderwidth=1,
            focusthickness=3,
            focuscolor=self.bg_color
        )
        style.map(
            "Custom.TButton",
            background=[('active', dark_gray)],
            foreground=[('disabled', medium_gray)]
        )

        # Créer le menu principal
        self.create_menu()

        # Organiser les boutons dans un cadre distinct
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(side=tk.TOP, pady=20)

        # Créer les boutons avec un fond gris et texte blanc
        self.btn_load_pdf = ttk.Button(
            button_frame, text="Charger un PDF", command=self.load_pdf,
            style="Custom.TButton", width=20
        )
        self.btn_load_image = ttk.Button(
            button_frame, text="Charger une Image", command=self.load_image,
            style="Custom.TButton", width=20
        )
        self.btn_capture_image = ttk.Button(
            button_frame, text="Capturer une Image", command=self.start_webcam_capture,
            style="Custom.TButton", width=20
        )
        self.btn_extract_text = ttk.Button(
            button_frame, text="Extraire le Texte", command=self.extract_text,
            style="Custom.TButton", width=20
        )

        self.btn_load_pdf.grid(row=0, column=0, padx=5, pady=5)
        self.btn_load_image.grid(row=0, column=1, padx=5, pady=5)
        self.btn_capture_image.grid(row=0, column=2, padx=5, pady=5)
        self.btn_extract_text.grid(row=0, column=4, padx=5, pady=5)

        # Création du cadre pour l'affichage de la webcam
        self.webcam_frame = tk.Frame(self.root, bg=self.bg_color)
        self.webcam_frame.pack(side=tk.TOP, pady=10)

        # Zone d'affichage de l'image
        self.panel_image = tk.Label(self.webcam_frame, bg=self.bg_color, width=600, height=400)
        self.panel_image.pack()

    def create_menu(self):
        """Créer le menu principal de l'application."""
        menu = tk.Menu(self.root, bg=self.bg_color, fg=self.fg_color)
        self.root.config(menu=menu)

        # Menu 'Fichier'
        file_menu = tk.Menu(menu, tearoff=0, bg=self.bg_color, fg=self.fg_color)
        menu.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Charger un PDF", command=self.load_pdf)
        file_menu.add_command(label="Charger une Image", command=self.load_image)
        file_menu.add_command(label="Capturer une Image", command=self.start_webcam_capture)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.root.quit)

        # Menu 'Aide'
        help_menu = tk.Menu(menu, tearoff=0, bg=self.bg_color, fg=self.fg_color)
        menu.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="À propos", command=self.show_about_info)

        # Menu 'Préférences'
        settings_menu = tk.Menu(menu, tearoff=0, bg=self.bg_color, fg=self.fg_color)
        menu.add_cascade(label="Préférences", menu=settings_menu)
        settings_menu.add_command(label="Langue OCR", command=self.show_preferences)

    def load_pdf(self):
        """Charger un fichier PDF et en extraire le texte."""
        # Réinitialiser l'affichage de l'image et du texte
        self.clear_status()
        self.clear_image()
        self.source_type = "loaded_pdf"

        # Ouvrir le dialogue pour sélectionner un fichier PDF
        self.file_path = filedialog.askopenfilename(
            title="Choisir un fichier PDF",
            filetypes=[("PDF Files", "*.pdf")],
        )

        # Réinitialiser l'image traitée
        self.image = None
        self.processed_image = None

        # Afficher l'image du pdf dans l'interface
        if self.file_path:
            images = convert_pdf_to_images(self.file_path)
            for image in images:
                image_np = np.array(image)

                cv_image = convert_to_cv_image(image_np)
                save_image(cv_image, f"../data/output/{self.source_type}.png")

                self.image = convert_to_grayscale(image_np)
                save_image(self.image, f"../data/output/processed_{self.source_type}.png")

                self.display_image(self.image)

    def load_image(self):
        """Charger une image depuis le système de fichiers."""
        # Réinitialiser l'affichage de l'image et du texte
        self.clear_status()
        self.clear_image()
        self.source_type = "loaded_image"

        # Ouvrir le dialogue pour sélectionner une image
        self.file_path = filedialog.askopenfilename(
            title="Choisir une image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")],
        )

        # Réinitialiser l'image traitée
        self.image = None
        self.processed_image = None

        # Charger l'image et l'afficher
        if self.file_path:
            self.image = load_image(self.file_path)
            save_image(self.image, f"../data/output/{self.source_type}.png")

            self.processed_image = process_image(self.image)
            save_image(self.processed_image, f"../data/output/processed_{self.source_type}.png")

            self.display_image(self.image)

    def start_webcam_capture(self):
        """Démarrer la capture d'image via la webcam."""
        # Réinitialiser l'affichage de l'image et le texte
        self.clear_status()
        self.clear_image()
        self.source_type = "captured_image"

        # Créer un thread séparé pour la capture de la webcam
        webcam_thread = threading.Thread(target=self.capture_from_webcam)
        webcam_thread.start()

    def capture_from_webcam(self):
        """Fonction pour capturer l'image depuis la webcam."""
        self.cap = load_webcam()
        folder = "../data/output"

        while True:
            frame = read_frame(self.cap)

            # Réinitialiser l'image traitée
            self.image = None
            self.processed_image = None

            # Affichage la frame en temps réel
            self.display_frame(frame)

            # Si on a une commande de capture ou de quitter, on la traite ici
            if hasattr(self, 'capture_command'):
                if self.capture_command == 'capture':
                    # Sauvegarder l'image capturée
                    self.file_path = f"{folder}/{self.source_type}.png"
                    save_image(frame, self.file_path)

                    # Charger et traiter l'image capturée
                    self.image = load_image(self.file_path)
                    self.processed_image = process_image(self.image)
                    save_image(self.processed_image, f"{folder}/processed_{self.source_type}.png")

                    # Afficher l'image dans l'interface
                    self.display_image(self.processed_image)
                    break
                elif self.capture_command == 'quit':
                    break

        release_webcam(self.cap)

        # Supprimer les boutons après la capture ou la sortie
        if hasattr(self, 'capture_frame') and self.capture_frame.winfo_ismapped():
            self.capture_frame.pack_forget()

    def capture_image(self):
        """Déclenche la commande de capture."""
        self.capture_command = 'capture'

    def quit_capture(self):
        """Déclenche la commande de quitter."""
        self.capture_command = 'quit'

    def create_capture_buttons(self):
        """Create buttons for capturing or quitting the webcam session."""
        if self.capture_frame is None:
            self.capture_frame = tk.Frame(self.root, bg=self.bg_color)
            self.capture_frame.pack(pady=10)

            self.capture_button = ttk.Button(
                self.capture_frame, text="Capturer", command=self.capture_image,
                style="Custom.TButton", width=15
            )
            self.capture_button.pack(side=tk.LEFT, padx=5, pady=5)

            self.quit_button = ttk.Button(
                self.capture_frame, text="Quitter", command=self.quit_capture,
                style="Custom.TButton", width=15
            )
            self.quit_button.pack(side=tk.LEFT, padx=5, pady=5)

    def display_frame(self, frame):
        """Display a video frame in the interface."""
        np_image = convert_to_np_image(frame)
        self.display_image(np_image)

        # Créer les boutons de capture si ce n'est pas déjà fait
        if self.capture_frame is None:
            self.create_capture_buttons()
        elif not self.capture_frame.winfo_ismapped():
            self.create_capture_buttons()

    def display_image(self, cv_image):
        """Afficher une image dans l'interface utilisateur."""
        np_image = convert_to_np_image(cv_image)
        image_pil = Image.fromarray(np_image)

        max_size = (600, 400)
        image_pil.thumbnail(max_size, Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(image_pil)

        self.panel_image.configure(image=image_tk)
        self.panel_image.image = image_tk

    def extract_text(self):
        """Extraire le texte du pdf ou de l'image."""
        self.clear_status()

        # Démarrer la barre de progression
        self.progress = ttk.Progressbar(
            self.root, orient=tk.HORIZONTAL, length=400, mode='indeterminate'
        )
        self.progress.pack(pady=10)
        self.progress.start()

        # Determiner la source et extraire le texte
        if self.file_path:
            self.root.after(
                100, lambda: self.complete_text_extraction(self.extract_text_from_pdf())
            )
        elif self.processed_image is not None:
            self.root.after(
                100, lambda: self.complete_text_extraction(self.extract_text_from_image())
            )
        else:
            messagebox.showerror("Erreur", "Impossible d'extraire le texte.")

    def extract_text_from_pdf(self):
        """Extraction du texte du pdf."""
        try:
            return extract_text_from_pdf(self.file_path)
        except Exception as e:
            print(f"Erreur lors de l'extraction du texte du PDF : {e}")
            messagebox.showerror("Erreur", f"Impossible d'extraire le texte du PDF.\n{str(e)}")
            return ""

    def extract_text_from_image(self):
        """Extraction du texte de l'image."""
        try:
            # text = pytesseract.image_to_string(self.processed_image)
            return ocr_from_image(self.processed_image)
        except Exception as e:
            print(f"Erreur lors de l'extraction du texte de l'image : {e}")
            messagebox.showerror("Erreur", f"Impossible d'extraire le texte de l'image.\n{str(e)}")
            return ""

    def complete_text_extraction(self, extracted_text):
        """Compléter l'extraction du texte et mettre à jour l'interface utilisateur."""
        # Arrêter et masquer la barre de progression
        if self.progress:
            self.progress.stop()
            self.progress.pack_forget()
            self.progress = None

        # Afficher le texte extrait dans un nouveau cadre de texte
        self.text_frame = tk.Frame(self.root, bg=self.bg_color)
        self.text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(self.text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_output = tk.Text(
            self.text_frame, height=10, wrap=tk.WORD, yscrollcommand=scrollbar.set,
            bg="white", fg=self.fg_color, font=("Helvetica", 10), borderwidth=1, relief="solid"
        )
        self.text_output.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_output.yview)

        self.text_output.insert(tk.END, extracted_text)

        # Sauvegarder le texte extrait dans un fichier .txt, même si le texte est vide
        self.save_text_to_file(extracted_text)

        # Afficher le label indiquant que l'extraction est terminée
        self.status_label = tk.Label(
            self.root, text="Extraction du texte effectuée", bg=self.bg_color, fg=self.fg_color
        )
        self.status_label.pack(pady=10)

    def clear_status(self):
        """Supprimer la barre de progression et le label de statut s'ils existent."""
        # Supprimer la barre de progression si elle existe
        if hasattr(self, 'progress') and self.progress is not None:
            if self.progress.winfo_exists():
                self.progress.destroy()
            self.progress = None

        # Supprimer le label de statut s'il existe
        if hasattr(self, 'status_label') and self.status_label is not None:
            if self.status_label.winfo_exists():
                self.status_label.destroy()
            self.status_label = None

        # Supprimer le contenu de l'ancien cadre de texte si text_output est toujours présent
        if hasattr(self, 'text_output') and self.text_output is not None:
            try:
                self.text_output.delete(1.0, tk.END)
            except tk.TclError:
                pass
            self.text_output = None

        # Supprimer ou masquer le cadre de texte s'il existe
        if hasattr(self, 'text_frame') and self.text_frame is not None:
            if self.text_frame.winfo_exists():
                self.text_frame.destroy()
            self.text_frame = None

    def clear_image(self):
        """Efface l'image affichée, si nécessaire."""
        if hasattr(self, 'panel_image') and self.panel_image is not None:
            self.panel_image.configure(image='')
            self.panel_image.image = None

    def show_about_info(self):
        """Afficher une boîte de dialogue À propos."""
        messagebox.showinfo(
            "À propos", "Cette application permet de capturer des images, "
                        "d'analyser des formes et des signatures, et d'extraire du texte via OCR."
        )

    def show_preferences(self):
        """Afficher la fenêtre de préférences."""
        pref_window = tk.Toplevel(self.root)
        pref_window.title("Préférences")
        pref_window.geometry("300x150")

        # Exemple de choix de langue pour l'OCR
        lang_label = tk.Label(pref_window, text="Langue pour l'OCR :")
        lang_label.pack(pady=5)
        lang_option = ttk.Combobox(pref_window, values=["en", "fr", "sp", "de"])
        lang_option.set(self.ocr_language)
        lang_option.pack(pady=5)

        save_button = ttk.Button(
            pref_window, text="Sauvegarder",
            command=lambda: self.save_preferences(lang_option.get())
        )
        save_button.pack(pady=10)

    def save_preferences(self, language):
        """Sauvegarder les préférences utilisateur."""
        self.ocr_language = language
        messagebox.showinfo("Préférences", "Les préférences ont été sauvegardées.")

    def save_text_to_file(self, text):
        """Enregistrer le texte extrait dans un fichier .txt avec un nom basé sur la source."""
        # Créer un nom de fichier par défaut basé sur la source
        default_filename = f"{self.source_type}_extracted_text.txt"
        folder = "../data/output"
        output_path = f"{folder}/{default_filename}"

        # Ouvrir une boîte de dialogue pour choisir où sauvegarder le fichier
        self.file_path = filedialog.asksaveasfilename(
            initialfile=default_filename,
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Enregistrer sous"
        )

        # Si l'utilisateur a choisi un fichier, enregistrer le texte
        if self.file_path:
            try:
                save_text(text, output_path)
                print(f"Chemin du texte sauvegardé: {output_path}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de sauvegarder le texte : {e}")



if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
