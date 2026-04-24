from regipy.registry import RegistryHive
from typing import Any, Dict
from .base import BaseForensicTool

class RegistryParser(BaseForensicTool):
    async def analyze(self, file_path: str) -> Dict[str, Any]:
        try:
            reg = RegistryHive(file_path)
            # We'll extract some interesting basic info for the demo
            # A full implementation would traverse more deeply
            root_key = reg.root_key
            
            # Get some basic stats or common persistence keys
            persistence_keys = [
                r"Software\Microsoft\Windows\CurrentVersion\Run",
                r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
            ]
            
            found_keys = []
            for key_path in persistence_keys:
                key = reg.get_key(key_path)
                if key:
                    values = [v.to_dict() for v in key.get_values()]
                    found_keys.append({
                        "path": key_path,
                        "values": values
                    })

            return {
                "tool": self.tool_name,
                "hive_type": reg.hive_type,
                "persistence_keys": found_keys
            }
        except Exception as e:
            return {"error": f"Failed to parse registry: {str(e)}"}

    @property
    def tool_name(self) -> str:
        return "RegistryParser"
