import json
import sys
import webbrowser
import os


# Couleurs utilisées pour les classes dans le diagramme Mermaid
CLASS_COLORS = {
    "main": "#add8e6",    # Bleu clair pour la classe principale
    "nested": "#90ee90"  # Vert clair pour les classes imbriquées (nested)
}

def _build_class_and_nested_definitions(class_name, properties, all_class_definitions, all_relations, class_styles):
    """Construit les définitions de classe et gère les propriétés imbriquées (nested)."""
    current_class_lines = []
    current_class_lines.append(f"    class {class_name} {{")

    # Ajout de toutes les propriétés simples (non-nested)
    for field_name, field_props in properties.items():
        field_type = field_props.get("type", "unknown")
        if field_type != "nested":
            current_class_lines.append(f"        +{field_type} {field_name}")
    
    # Gère les propriétés de type 'nested' et crée les relations associées
    for field_name, field_props in properties.items():
        field_type = field_props.get("type", "unknown")
        if field_type == "nested":
            nested_class_name = field_name.capitalize()
            # Ajoute une relation entre la classe parente et la classe imbriquée
            all_relations.append(f'    {class_name} "1" -- "*" {nested_class_name} : contains')
            
            if "properties" in field_props:
                class_styles[nested_class_name] = CLASS_COLORS["nested"]
                _build_class_and_nested_definitions(nested_class_name, field_props["properties"], all_class_definitions, all_relations, class_styles)
    current_class_lines.append(f"    }}")
    all_class_definitions.extend(current_class_lines)

def convert_es_mapping_to_mermaid(json_data):
    """Convertit les données de mappage Elasticsearch en code de diagramme Mermaid."""
    mermaid_diagram_parts = ["classDiagram"]
    all_class_definitions = []
    all_relations = []
    class_styles = {}

    mappings = json_data.get("mappings", {})

    main_class_name = "Document"
    properties_data = None

    # Tente de trouver les propriétés de niveau supérieur ou un mappage de type spécifique (ex: "products")
    if "properties" in mappings:
        properties_data = mappings["properties"]
    else:
        # Si un mappage de type spécifique est présent, utilise son nom comme classe principale
        for key, value in mappings.items():
            if isinstance(value, dict) and "properties" in value:
                main_class_name = key.capitalize()
                properties_data = value["properties"]
                break

    if not properties_data:
        return "Erreur : Aucune propriété trouvée dans le mappage."
    
    class_styles[main_class_name] = CLASS_COLORS["main"]
    _build_class_and_nested_definitions(main_class_name, properties_data, all_class_definitions, all_relations, class_styles)
    
    # Ajoute les styles de classe au début du diagramme
    for cls_name, color in class_styles.items():
        mermaid_diagram_parts.append(f"    style {cls_name} fill:{color}")

    # Ajoute une ligne vide pour une meilleure lisibilité entre les styles et les définitions/relations
    if class_styles or all_class_definitions or all_relations: 
        mermaid_diagram_parts.append("")

    mermaid_diagram_parts.extend(all_class_definitions)
    mermaid_diagram_parts.extend(all_relations)

    return "\n".join(mermaid_diagram_parts)

def display_mermaid_diagram_in_browser(mermaid_code):
    """Lit le template HTML, insère le code Mermaid, l'enregistre et l'ouvre dans le navigateur."""
    # Chemin vers le fichier template HTML
    html_template_file = "index.html"
    
    try:
        with open(html_template_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"Erreur: Le fichier template HTML '{html_template_file}' est introuvable. Veuillez vous assurer qu'il existe dans le même répertoire que le script.")
        return

    # Remplacer le marqueur par le code Mermaid
    updated_html_content = html_content.replace("<!-- MERMAID_CODE_HERE -->", mermaid_code)

    # Écrire le contenu mis à jour dans le même fichier index.html
    with open(html_template_file, 'w', encoding='utf-8') as f:
        f.write(updated_html_content)

    try:
        webbrowser.open(f'file://{os.path.abspath(html_template_file)}')
    except Exception as e:
        print(f"Erreur lors de l'ouverture du navigateur : {e}")
        print(f"Veuillez ouvrir le fichier manuellement : {os.path.abspath(html_template_file)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Utilisation: python es_mapping_to_mermaid.py <chemin_vers_fichier_json_de_mapping>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    
    try:
        with open(json_file_path, 'r') as f:
            mapping_data = json.load(f)
        
        mermaid_output = convert_es_mapping_to_mermaid(mapping_data)
        display_mermaid_diagram_in_browser(mermaid_output)

    except FileNotFoundError:
        print(f"Erreur : Fichier non trouvé à {json_file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Erreur : Format JSON invalide dans {json_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
        sys.exit(1) 

