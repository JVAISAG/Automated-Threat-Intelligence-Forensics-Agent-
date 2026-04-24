import operator
from typing import Annotated, TypedDict, Dict, Any, List

class AgentState(TypedDict):
    file_path: str
    file_hash: str
    metadata: Dict[str, Any]
    analysis_route: str  # 'memory_malware' or 'system_registry'
    raw_artifacts: Annotated[List[Dict[str, Any]], operator.add]
    final_report: str
    is_cached: bool
