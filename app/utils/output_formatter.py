# utils/output_formatter.py

import yaml

def pretty_print_yaml(yaml_text: str) -> str:
    """
    Converts YAML string to a clean, readable text format.
    """
    try:
        parsed = yaml.safe_load(yaml_text)
        return format_dict(parsed)
    except yaml.YAMLError:
        return yaml_text  # Return as-is if it's not valid YAML

def format_dict(data, indent=0) -> str:
    """
    Recursively formats a dictionary into readable bullet points.
    """
    result = ""
    space = "  " * indent
    bullet = "- "
    
    if isinstance(data, dict):
        for key, value in data.items():
            result += f"{space}{key.capitalize()}:\n{format_dict(value, indent + 1)}"
    elif isinstance(data, list):
        for item in data:
            result += f"{space}{bullet}{format_dict(item, indent + 1).strip()}\n"
    else:
        result += f"{space}{data}\n"

    return result
