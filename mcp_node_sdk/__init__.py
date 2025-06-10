"""
MCP Node SDK - Standard library for building MCP-compatible model nodes.

This SDK provides the base classes and utilities needed to create
model nodes that integrate seamlessly with the MCP simulation platform.
"""

__version__ = "0.1.0"

from .base import ModelNode, ModelCapability, ExecutionContext, MCPResponse
from .validation import validate_metadata, validate_input, validate_output
from .decorators import capability, input_schema, output_schema
from .exceptions import (
    MCPNodeError, 
    ValidationError, 
    ExecutionError, 
    ConfigurationError
)

__all__ = [
    "ModelNode",
    "ModelCapability", 
    "ExecutionContext",
    "MCPResponse",
    "validate_metadata",
    "validate_input", 
    "validate_output",
    "capability",
    "input_schema",
    "output_schema",
    "MCPNodeError",
    "ValidationError",
    "ExecutionError",
    "ConfigurationError",
]