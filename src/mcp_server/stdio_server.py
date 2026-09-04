import sys
import os
import json
import logging
import traceback
from typing import Any, Dict

# Ensure src is in the python path so xingce_solver can be imported
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from .registry import ToolRegistry
from .tools import get_all_tools
from .bridge import XingceBridge
from .runtime_adapter import XingceRuntimeAdapter
from xingce_solver import mcp_server as xingce_runtime

# Setup minimal logging to stderr so it doesn't pollute stdout (JSON-RPC)
logging.basicConfig(level=logging.ERROR, stream=sys.stderr)
logger = logging.getLogger(__name__)

def main():
    # Initialize core components
    registry = ToolRegistry()
    for tool in get_all_tools():
        registry.register(tool)

    adapter = XingceRuntimeAdapter(xingce_runtime)
    bridge = XingceBridge(mcp_runtime=adapter)
    
    # Read from stdin continuously
    while True:
        try:
            raw_line = sys.stdin.buffer.readline()
            if not raw_line:
                break
            
            line = raw_line.decode('utf-8', errors='replace').strip()
            if not line:
                continue
                
            try:
                msg = json.loads(line)
            except json.JSONDecodeError:
                continue
                
            if "method" not in msg:
                continue
                
            method = msg["method"]
            msg_id = msg.get("id")
            
            response: Dict[str, Any] = {"jsonrpc": "2.0", "id": msg_id}
            
            try:
                if method == "initialize":
                    response["result"] = {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "xingce-mcp-stdio", "version": "1.0.0"}
                    }
                elif method == "notifications/initialized":
                    continue # No response needed
                elif method == "tools/list":
                    response["result"] = {
                        "tools": registry.list_tools()
                    }
                elif method == "tools/call":
                    params = msg.get("params", {})
                    tool_name = params.get("name")
                    args = params.get("arguments", {})
                    
                    # Use bridge to dispatch
                    result = bridge.call(tool_name, args)
                    
                    result_text = json.dumps(result, ensure_ascii=False) if not isinstance(result, str) else result
                    response["result"] = {
                        "content": [
                            {
                                "type": "text",
                                "text": result_text
                            }
                        ],
                        "isError": False
                    }
                else:
                    response["error"] = {"code": -32601, "message": f"Method not found: {method}"}
                    
            except Exception as e:
                logger.error(f"Error processing {method}: {e}", exc_info=True)
                response["error"] = {"code": -32000, "message": str(e)}
            
            if msg_id is not None:
                # Write back to stdout using UTF-8 explicitly
                response_str = json.dumps(response, ensure_ascii=False) + "\n"
                sys.stdout.buffer.write(response_str.encode('utf-8'))
                sys.stdout.buffer.flush()
                
        except Exception as e:
            logger.error(f"Loop error: {e}", exc_info=True)

if __name__ == "__main__":
    main()
