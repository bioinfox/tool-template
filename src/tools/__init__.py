import inspect, os, sys
from typing import List

from ..type import Tool


_TOOLS: List[Tool] = []
_tool_dir = os.path.dirname(__file__)
modules = [os.path.splitext(_file)[0] for _file in os.listdir(_tool_dir) if not _file.startswith('__')]
for mod_name in modules:
    exec(f"from .{mod_name} import *")
    module = sys.modules[f"{__name__}.{mod_name}"]
    tools = [x for x in inspect.getmembers(module) if inspect.isclass(x[1]) and issubclass(x[1], Tool) and x[1] != Tool]
    _TOOLS.extend([x[1]() for x in tools])


def get_tool(name: str) -> Tool:
    return next(filter(lambda p: p.name == name, _TOOLS), None)


def get_tools() -> List[Tool]:
    return _TOOLS
