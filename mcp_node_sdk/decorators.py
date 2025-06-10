"""
Decorators for MCP nodes.
"""

from .base import capability, ModelCapability

# Re-export decorators
__all__ = ["capability", "input_schema", "output_schema"]

def input_schema(schema):
    """Decorator to define input schema for a capability."""
    def decorator(func):
        if not hasattr(func, '_mcp_capability'):
            func._mcp_capability = ModelCapability(name=func.__name__)
        func._mcp_capability.input_schema = schema
        return func
    return decorator

def output_schema(schema):
    """Decorator to define output schema for a capability."""
    def decorator(func):
        if not hasattr(func, '_mcp_capability'):
            func._mcp_capability = ModelCapability(name=func.__name__)
        func._mcp_capability.output_schema = schema
        return func
    return decorator