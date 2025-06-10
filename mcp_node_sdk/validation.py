"""
Validation utilities for MCP nodes.
"""

import json
import jsonschema
from pathlib import Path
from typing import Dict, Any

from .exceptions import ValidationError


def load_schema(schema_name: str) -> Dict[str, Any]:
    """Load a JSON schema from the schemas directory."""
    schema_path = Path(__file__).parent / "schemas" / f"{schema_name}.schema.json"
    
    if not schema_path.exists():
        raise ValidationError(f"Schema file not found: {schema_path}")
    
    try:
        with open(schema_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValidationError(f"Invalid JSON in schema {schema_name}: {e}")


def validate_metadata(metadata: Dict[str, Any]) -> None:
    """Validate node metadata against the schema."""
    schema = load_schema("metadata")

    try:
        jsonschema.validate(metadata, schema)
    except jsonschema.ValidationError as e:
        raise ValidationError(f"Metadata validation failed: {e.message}")


def validate_input(input_data: Dict[str, Any], schema: Dict[str, Any]) -> None:
    """Validate input data against a JSON schema."""
    try:
        jsonschema.validate(input_data, schema)
    except jsonschema.ValidationError as e:
        raise ValidationError(f"Input validation failed: {e.message}")


def validate_output(output_data: Dict[str, Any], schema: Dict[str, Any]) -> None:
    """Validate output data against a JSON schema."""
    try:
        jsonschema.validate(output_data, schema)
    except jsonschema.ValidationError as e:
        raise ValidationError(f"Output validation failed: {e.message}")
