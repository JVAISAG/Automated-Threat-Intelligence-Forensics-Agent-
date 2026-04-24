from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseForensicTool(ABC):
    """Abstract base class for all forensic analysis tools."""
    
    @abstractmethod
    async def analyze(self, file_path: str) -> Dict[str, Any]:
        """Execute the forensic logic on the target file."""
        pass

    @property
    @abstractmethod
    def tool_name(self) -> str:
        pass
