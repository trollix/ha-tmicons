import os
import xml.etree.ElementTree as ET
import json

def process_svg_directory(input_directory, output_json_file):
    # Crée une structure de données pour stocker les informations extraites
    svg_data = {"elements": []}

    # Parcours tous les fichiers du répertoire d'entrée
    for filename in os.listdir(input_directory):
        if filename.endswith(".svg"):
            svg_file_path = os.path.join(input_directory, filename)

            # Retire l'extension ".svg" du nom du fichier
            filename_without_extension = os.path.splitext(filename)[0]
            
            # Parse le fichier SVG
            tree = ET.parse(svg_file_path)
            root = tree.getroot()

            # Parcours les éléments du fichier SVG
            '''
            for element in root.iter():
                d_value = element.attrib.get("d", "")
                if d_value:  # Ne conserver que si l'attribut "d" n'est pas vide
                    svg_data[filename_without_extension] = {"d": d_value}
                    '''

            # Parcours les éléments du fichier SVG
            for element in root.iter():
                d_value = element.attrib.get("d", "")
                if d_value:  # Ne conserver que si l'attribut "d" n'est pas vide
                    svg_data[filename_without_extension] = {"path": d_value, "keyword": []}


    # Supprime la clé "elements" si elle est présente
    svg_data.pop("elements", None)

    # Écrit les données dans un fichier JSON avec la structure souhaitée
    with open(output_json_file, "w") as json_output:
        json_output.write("const TMICONS_MAP = {\n\n")
        for key, value in svg_data.items():
            json_output.write(f'  "{key}": {json.dumps(value, indent=2)},\n')
        json_output.write("};\n")




if __name__ == "__main__":
    input_svg_directory = "./icons/SVG"
    output_json_file = "./outputs.json"

    process_svg_directory(input_svg_directory, output_json_file)
