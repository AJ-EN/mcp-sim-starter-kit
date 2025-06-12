from mcp_node_sdk import ModelNode, capability, ExecutionContext
import json
from pathlib import Path

class __NODE_CLASS__(ModelNode):
    @property
    def metadata(self):
        # Load metadata from JSON file
        metadata_path = Path(__file__).parent / "metadata.json"
        if metadata_path.exists():
            return json.loads(metadata_path.read_text())
        else:
            # Fallback metadata
            return {
                "model_id": "__NODE_ID__",
                "name": "__NODE_NAME__",
                "version": "0.1.0",
                "capabilities": ["simulate"],
                "endpoints": {"execute": "/mcp/execute", "health": "/health"},
                "cost_per_call": 1.0
            }
    
    async def initialize(self):
        """Initialize the model (load data, set parameters, etc.)"""
        pass
    
    async def cleanup(self):
        """Cleanup resources when shutting down"""
        pass
    
    @capability(name="simulate")
    async def simulate(self, ctx: ExecutionContext):
        """Default simulation capability - replace with your logic"""
        return {"echo": ctx.input_data}

if __name__ == "__main__":
    import asyncio
    import uvicorn
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    node = __NODE_CLASS__()
    
    @app.on_event("startup")
    async def startup():
        await node.initialize()
    
    @app.on_event("shutdown") 
    async def shutdown():
        await node.cleanup()
    
    @app.get("/health")
    async def health():
        health_response = await node.health_check()
        return JSONResponse(content=health_response.to_dict())
    
    @app.get("/metadata")
    async def get_metadata():
        return JSONResponse(content=node.metadata)
    
    @app.post("/mcp/execute")
    async def execute(request: dict):
        context = ExecutionContext(
            request_id=request.get("request_id", "unknown"),
            capability=request.get("capability"),
            input_data=request.get("input_data", {})
        )
        response = await node.execute(context)
        return JSONResponse(content=response.to_dict())
    
    print(f"Starting {node.metadata['name']} on port 5000...")
    uvicorn.run(app, host="0.0.0.0", port=5000)