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

