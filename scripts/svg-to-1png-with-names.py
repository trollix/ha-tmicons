import os
import io
import cairosvg
from PIL import Image, ImageDraw, ImageFont

def chunks(lst, chunk_size):
    """Divise la liste en morceaux de taille chunk_size."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def convert_svg_to_single_png(input_directory, output_path, columns=10, spacing=10):
    # Crée une liste pour stocker les images PNG individuelles
    images = []
    icon_names = []  # Ajout de la liste pour stocker les noms des icônes

    # Parcours tous les fichiers du répertoire d'entrée
    for filename in os.listdir(input_directory):
        if filename.endswith(".svg"):
            # Construit le chemin complet du fichier SVG
            input_path = os.path.join(input_directory, filename)

            # Convertit le fichier SVG en image PNG
            with open(input_path, "rb") as svg_file:
                png_data = cairosvg.svg2png(file_obj=svg_file)

            # Convertit les données PNG en objet Image
            png_image = Image.open(io.BytesIO(png_data))
            images.append(png_image)
            icon_names.append(os.path.splitext(filename)[0])  # Récupère le nom sans extension

    # Divise la liste des images et des noms en groupes de 'columns'
    image_groups = list(chunks(images, columns))
    name_groups = list(chunks(icon_names, columns))

    # Crée une liste pour stocker les images concaténées horizontalement
    combined_images = []

    # Concatène les images et les noms horizontalement dans chaque groupe
    for i, group in enumerate(image_groups):
        max_height = max(image.height for image in group)
        total_width = sum(image.width + spacing for image in group) + (columns - 1) * spacing
        combined_image_horizontal = Image.new("RGBA", (total_width, max_height + 30), (255, 255, 255, 0))

        x_offset = spacing  # Ajout de la marge avant la première image
        for j, (image, icon_name) in enumerate(zip(group, name_groups[i])):
            combined_image_horizontal.paste(image, (x_offset, 0))

            # Ajoute le nom de l'icône sous l'image
            draw = ImageDraw.Draw(combined_image_horizontal)
            font = ImageFont.load_default()  # Vous pouvez ajuster la police si nécessaire

            # Calcul des dimensions du texte avec sauts de ligne
            text_bbox = draw.textbbox((x_offset, image.height + 5), icon_name, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

            # Positionnement du texte sous l'image avec une petite marge
            text_position = (x_offset + (image.width - text_width) / 2, image.height + 5)

            draw.text(text_position, icon_name, (0, 0, 0), font=font)

            x_offset += image.width + spacing

        combined_images.append(combined_image_horizontal)

    # Concatène les groupes d'images verticalement
    combined_image_vertical = Image.new("RGBA", (max(image.width for image in combined_images), sum(image.height for image in combined_images)))
    y_offset = 0
    for image_horizontal in combined_images:
        combined_image_vertical.paste(image_horizontal, (0, y_offset))
        y_offset += image_horizontal.height

    # Sauvegarde l'image combinée
    combined_image_vertical.save(output_path, format="PNG")

if __name__ == "__main__":
    input_directory = "./icons2/SVG"
    output_path = "./dist/icons_combined_with_names_columns.png"

    convert_svg_to_single_png(input_directory, output_path, columns=10, spacing=80)
