


def save_text(text: str, text_path: str) -> None:
    """Sauvegarde le texte extrait dans un fichier texte."""
    with open(text_path, 'w', encoding='utf-8') as file:
        if text.strip():
            file.write(text)
        else:
            file.write("Aucun texte n'a été extrait de cette image.")