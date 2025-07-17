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

