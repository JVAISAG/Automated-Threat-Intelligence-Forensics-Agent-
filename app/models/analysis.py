from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class AnalysisReport(BaseModel):
    file_name: str
    file_hash: str
    metadata: Dict[str, Any]
    raw_artifacts: List[Dict[str, Any]]
    final_report: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AnalysisResponse(BaseModel):
    status: str
    is_cached: bool
    data: AnalysisReport
