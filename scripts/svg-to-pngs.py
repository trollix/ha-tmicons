# pylint: skip-file
import os
import cairosvg

def convert_svg_to_png(input_directory, output_directory):
    # Vérifie si le répertoire de sortie existe, sinon le crée
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Parcours tous les fichiers du répertoire d'entrée
    for filename in os.listdir(input_directory):
        if filename.endswith(".svg"):
            # Construit les chemins complets d'entrée et de sortie
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".png")

            # Convertit le fichier SVG en PNG
            with open(input_path, "rb") as svg_file:
                cairosvg.svg2png(file_obj=svg_file, write_to=output_path)

if __name__ == "__main__":
    input_directory = "./icons2/SVG"
    output_directory = "./dist/icons2/PNG"

    convert_svg_to_png(input_directory, output_directory)
