from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, List

from .tools import get_tools, get_tool
from .type import Tool


router = APIRouter(prefix="/tools", tags=["Tool"])


@router.get("", response_model=List[Tool])
async def list_tools():
    return get_tools()


class ArgsRequest(BaseModel):
    name: str
    args: str


@router.post("/run", response_model=Any)
async def run_tool(request: ArgsRequest):
    tool_name, args = request.name, request.args
    tool = get_tool(tool_name)
    if tool is None:
        raise HTTPException(status_code=404, detail=f"Tool {tool_name} not found!")

    result = tool.run(args)
    if result is None:
        raise HTTPException(status_code=400, detail=f"Tool {tool_name} failed to run!")

    return result
