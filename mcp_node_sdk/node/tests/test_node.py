import pytest
import asyncio
import sys
import os

# Add parent directory to path to import node
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from node import __NODE_CLASS__
from mcp_node_sdk import ExecutionContext

@pytest.mark.asyncio
async def test_node_basic_functionality():
    """Test basic node functionality."""
    node = __NODE_CLASS__()
    await node.initialize()
    
    # Test health check
    health = await node.health_check()
    assert health.success
    
    # Test metadata
    metadata = node.metadata
    assert "model_id" in metadata
    assert "capabilities" in metadata
    
    # Test simulation capability
    context = ExecutionContext(
        request_id="test-123",
        capability="simulate",
        input_data={"input": "test data"}
    )
    
    response = await node.execute(context)
    assert response.success
    assert "echo" in response.data
    
    await node.cleanup()

@pytest.mark.asyncio
async def test_node_validation():
    """Test input validation."""
    node = __NODE_CLASS__()
    await node.initialize()
    
    # Test invalid capability
    context = ExecutionContext(
        request_id="test-456",
        capability="invalid_capability",
        input_data={}
    )
    
    response = await node.execute(context)
    assert not response.success
    
    await node.cleanup()