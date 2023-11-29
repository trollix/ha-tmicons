import os
import io
import cairosvg
from PIL import Image

def chunks(lst, chunk_size):
    """Divise la liste en morceaux de taille chunk_size."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def convert_svg_to_single_png(input_directory, output_path, columns=20):
    # Crée une liste pour stocker les images PNG individuelles
    images = []

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

    # Divise la liste des images en groupes de 'columns'
    image_groups = list(chunks(images, columns))

    # Crée une liste pour stocker les images concaténées horizontalement
    combined_images = []

    # Concatène les images horizontalement dans chaque groupe
    for group in image_groups:
        combined_image_horizontal = Image.new("RGBA", (sum(image.width for image in group), max(image.height for image in group)))
        x_offset = 0
        for image in group:
            combined_image_horizontal.paste(image, (x_offset, 0))
            x_offset += image.width
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
    output_path = "./dist/icons_combined.png"

    convert_svg_to_single_png(input_directory, output_path, columns=20)
