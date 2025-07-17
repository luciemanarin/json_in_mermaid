import json
import sys

def _build_class_and_nested_definitions(class_name, properties, all_class_definitions, all_relations):
    current_class_lines = []
    current_class_lines.append(f"    class {class_name} {{")

    # Ajout de toutes les propriétés simples
    for field_name, field_props in properties.items():
        field_type = field_props.get("type", "unknown")
        if field_type != "nested":
            current_class_lines.append(f"        +{field_type} {field_name}")
    
    # Gérer les propriétés imbriquées et leurs relations
    for field_name, field_props in properties.items():
        field_type = field_props.get("type", "unknown")
        if field_type == "nested":
            nested_class_name = field_name.capitalize()
            # Nous n'ajoutons pas les types imbriqués comme de simples propriétés ; ils sont gérés par la relation.
            all_relations.append(f"    {class_name} '1' -- '*' {nested_class_name} : contains")
            
            if "properties" in field_props:
                _build_class_and_nested_definitions(nested_class_name, field_props["properties"], all_class_definitions, all_relations)
    current_class_lines.append(f"    }}")
    all_class_definitions.extend(current_class_lines)

def convert_es_mapping_to_mermaid(json_data):
    mermaid_diagram_parts = ["classDiagram"]
    all_class_definitions = []
    all_relations = []

    mappings = json_data.get("mappings", {})

    main_class_name = "Document"
    properties_data = None

    # Essayer de trouver les propriétés de niveau supérieur ou un mappage de type spécifique
    if "properties" in mappings:
        properties_data = mappings["properties"]
    else:
        # Si un mappage de type spécifique (comme "products") est présent
        for key, value in mappings.items():
            if isinstance(value, dict) and "properties" in value:
                main_class_name = key.capitalize()
                properties_data = value["properties"]
                break

    if not properties_data:
        return "Error: No properties found in the mapping."
    
    _build_class_and_nested_definitions(main_class_name, properties_data, all_class_definitions, all_relations)
    
    mermaid_diagram_parts.extend(all_class_definitions)
    mermaid_diagram_parts.extend(all_relations)

    return "\n".join(mermaid_diagram_parts)


