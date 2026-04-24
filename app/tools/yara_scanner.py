import yara
import os
from typing import Any, Dict
from .base import BaseForensicTool
from ..core.config import settings

class YaraScanner(BaseForensicTool):
    def __init__(self, rules_path: str = settings.YARA_RULES_PATH):
        self.rules_path = rules_path
        self.rules = None
        if os.path.exists(self.rules_path):
            self.rules = yara.compile(filepath=self.rules_path)

    async def analyze(self, file_path: str) -> Dict[str, Any]:
        if not self.rules:
            return {"error": "YARA rules not found or not compiled."}
        
        matches = self.rules.match(file_path)
        results = []
        for match in matches:
            results.append({
                "rule": match.rule,
                "tags": match.tags,
                "meta": match.meta,
                "strings": [str(s) for s in match.strings]
            })
        
        return {
            "tool": self.tool_name,
            "matches_count": len(results),
            "matches": results
        }

    @property
    def tool_name(self) -> str:
        return "YaraScanner"
