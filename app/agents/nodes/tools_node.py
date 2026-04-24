from ..state import AgentState
from ...tools.yara_scanner import YaraScanner
from ...tools.registry_parser import RegistryParser

class ToolsNode:
    def __init__(self):
        self.yara = YaraScanner()
        self.registry = RegistryParser()

    async def yara_scan(self, state: AgentState):
        result = await self.yara.analyze(state["file_path"])
        return {"raw_artifacts": [result]}

    async def registry_parse(self, state: AgentState):
        result = await self.registry.analyze(state["file_path"])
        return {"raw_artifacts": [result]}
