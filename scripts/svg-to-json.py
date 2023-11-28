import xml.etree.ElementTree as ET
import json

def svg_to_json(svg_file, json_file):
    # Parse le fichier SVG
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Crée une structure de données pour stocker les informations extraites
    svg_data = {"elements": []}

    # Parcours les éléments du fichier SVG
    for element in root.iter():
        d_value = element.attrib.get("d", "")
        if d_value:  # Ne conserver que si l'attribut "d" n'est pas vide
            element_data = {"d": d_value}
            svg_data["elements"].append(element_data)

    # Écrit les données dans un fichier JSON
    with open(json_file, "w") as json_output:
        json.dump(svg_data, json_output, indent=2)


if __name__ == "__main__":
    svg_file_path = "./icons/drop.svg"
    json_file_path = "./output.json"
    
    svg_to_json(svg_file_path, json_file_path)
