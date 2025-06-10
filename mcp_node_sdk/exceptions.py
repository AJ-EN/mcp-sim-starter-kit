"""
Exception classes for MCP nodes.
"""


class MCPNodeError(Exception):
    """Base exception for MCP node errors."""
    pass


class ValidationError(MCPNodeError):
    """Raised when validation fails."""
    pass


class ExecutionError(MCPNodeError):
    """Raised when execution fails."""
    pass


class ConfigurationError(MCPNodeError):
    """Raised when configuration is invalid."""
    pass