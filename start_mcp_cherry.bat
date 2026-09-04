@echo off
cd /d "%~dp0"
python -m src.mcp_server.stdio_server
