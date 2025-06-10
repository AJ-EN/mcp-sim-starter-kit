"""
Base classes for MCP model nodes.
"""

import asyncio
import json
import logging
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional, Union, Callable
from datetime import datetime
import uuid

from .exceptions import ValidationError, ExecutionError, ConfigurationError
from .validation import validate_metadata, validate_input


@dataclass
class ExecutionContext:
    """Context information for a model execution."""
    request_id: str
    capability: str
    input_data: Dict[str, Any]
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if not self.request_id:
            self.request_id = str(uuid.uuid4())


@dataclass 
class MCPResponse:
    """Standard response format for MCP operations."""
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    execution_time_ms: Optional[float] = None
    cost: Optional[float] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert response to dictionary."""
        return {k: v for k, v in asdict(self).items() if v is not None}


class ModelCapability:
    """Decorator for defining model capabilities."""
    
    def __init__(
        self, 
        name: str,
        input_schema: Optional[Dict[str, Any]] = None,
        output_schema: Optional[Dict[str, Any]] = None,
        cost_estimate: Optional[float] = None,
        description: Optional[str] = None
    ):
        self.name = name
        self.input_schema = input_schema or {}
        self.output_schema = output_schema or {}
        self.cost_estimate = cost_estimate
        self.description = description
        
    def __call__(self, func: Callable) -> Callable:
        """Mark function as a model capability."""
        func._mcp_capability = self
        return func


class ModelNode(ABC):
    """
    Base class for all MCP model nodes.
    
    This class provides the standard interface that all model nodes must implement.
    It handles registration, health checks, input validation, and execution routing.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.logger = logging.getLogger(self.__class__.__name__)
        self._capabilities: Dict[str, Callable] = {}
        self._metadata: Optional[Dict[str, Any]] = None
        self._discover_capabilities()
        
    def _discover_capabilities(self):
        """Discover capabilities by inspecting decorated methods."""
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, '_mcp_capability'):
                capability = attr._mcp_capability
                self._capabilities[capability.name] = attr
                self.logger.info(f"Discovered capability: {capability.name}")
    
    @property
    @abstractmethod
    def metadata(self) -> Dict[str, Any]:
        """Return the metadata describing this model node."""
        pass
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the model node (load models, connect to resources, etc.)."""
        pass
    
    @abstractmethod 
    async def cleanup(self) -> None:
        """Cleanup resources when shutting down."""
        pass
    
    async def validate_metadata(self) -> bool:
        """Validate that this node's metadata conforms to the schema."""
        try:
            validate_metadata(self.metadata)
            return True
        except ValidationError as e:
            self.logger.error(f"Metadata validation failed: {e}")
            return False
    
    async def health_check(self) -> MCPResponse:
        """Perform health check."""
        try:
            # Basic health checks
            checks = {
                "metadata_valid": await self.validate_metadata(),
                "capabilities_loaded": len(self._capabilities) > 0,
                "timestamp": datetime.utcnow().isoformat(),
            }
            
            # Allow subclasses to add custom health checks
            custom_checks = await self._custom_health_checks()
            checks.update(custom_checks)
            
            is_healthy = all(v for v in checks.values() if isinstance(v, bool))
            
            return MCPResponse(
                success=is_healthy,
                data={"health_checks": checks},
                metadata={"node_id": self.metadata.get("model_id")}
            )
            
        except Exception as e:
            self.logger.error(f"Health check failed: {e}")
            return MCPResponse(
                success=False,
                error=f"Health check failed: {str(e)}"
            )
    
    async def _custom_health_checks(self) -> Dict[str, Any]:
        """Override this to add custom health checks."""
        return {}
    
    async def execute(self, context: ExecutionContext) -> MCPResponse:
        """Execute a capability with the given context."""
        start_time = time.time()
        
        try:
            # Validate capability exists
            if context.capability not in self._capabilities:
                raise ExecutionError(
                    f"Unknown capability: {context.capability}. "
                    f"Available: {list(self._capabilities.keys())}"
                )
            
            # Get the capability handler
            handler = self._capabilities[context.capability]
            capability_info = handler._mcp_capability
            
            # Validate input if schema is defined
            if capability_info.input_schema:
                validate_input(context.input_data, capability_info.input_schema)
            
            # Execute the capability
            self.logger.info(
                f"Executing capability '{context.capability}' "
                f"for request {context.request_id}"
            )
            
            result = await self._execute_capability(handler, context)
            
            execution_time = (time.time() - start_time) * 1000
            
            return MCPResponse(
                success=True,
                data=result,
                execution_time_ms=execution_time,
                cost=capability_info.cost_estimate,
                metadata={
                    "capability": context.capability,
                    "request_id": context.request_id,
                    "node_id": self.metadata.get("model_id")
                }
            )
            
        except ValidationError as e:
            self.logger.error(f"Validation error: {e}")
            return MCPResponse(
                success=False,
                error=f"Input validation failed: {str(e)}",
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except ExecutionError as e:
            self.logger.error(f"Execution error: {e}")
            return MCPResponse(
                success=False,
                error=str(e),
                execution_time_ms=(time.time() - start_time) * 1000
            )
            
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            return MCPResponse(
                success=False,
                error=f"Internal error: {str(e)}",
                execution_time_ms=(time.time() - start_time) * 1000
            )
    
    async def _execute_capability(
        self, 
        handler: Callable, 
        context: ExecutionContext
    ) -> Dict[str, Any]:
        """Execute a capability handler."""
        if asyncio.iscoroutinefunction(handler):
            return await handler(context)
        else:
            # Run sync functions in thread pool
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(None, handler, context)
    
    def get_capability_info(self, capability_name: str) -> Optional[ModelCapability]:
        """Get information about a specific capability."""
        if capability_name in self._capabilities:
            return self._capabilities[capability_name]._mcp_capability
        return None
    
    def list_capabilities(self) -> List[str]:
        """List all available capabilities."""
        return list(self._capabilities.keys())


# Convenience function for creating capability decorator
def capability(
    name: str,
    input_schema: Optional[Dict[str, Any]] = None,
    output_schema: Optional[Dict[str, Any]] = None,
    cost_estimate: Optional[float] = None,
    description: Optional[str] = None
) -> ModelCapability:
    """Create a capability decorator."""
    return ModelCapability(
        name=name,
        input_schema=input_schema,
        output_schema=output_schema,
        cost_estimate=cost_estimate,
        description=description
    )