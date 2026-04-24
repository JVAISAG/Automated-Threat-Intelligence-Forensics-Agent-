from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from ...services.file_service import FileService
from ...core.database import get_database
from ...agents.graph import create_forensic_graph
from ...models.analysis import AnalysisReport, AnalysisResponse
from datetime import datetime

router = APIRouter()
graph = create_forensic_graph()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_file(file: UploadFile = File(...), db = Depends(get_database)):
    # 1. Save and Hash
    file_path = await FileService.save_upload(file)
    file_hash = await FileService.get_sha256(file_path)
    
    # 2. Check Cache
    cached_report = await db.analysis_sessions.find_one({"file_hash": file_hash})
    if cached_report:
        return AnalysisResponse(
            status="success",
            is_cached=True,
            data=AnalysisReport(**cached_report)
        )
    
    # 3. Run LangGraph Workflow
    initial_state = {
        "file_path": file_path,
        "file_hash": file_hash,
        "metadata": {
            "filename": file.filename,
            "content_type": file.content_type,
            "size": file.size
        },
        "raw_artifacts": [],
        "is_cached": False
    }
    
    final_state = await graph.ainvoke(initial_state)
    
    # 4. Log to MongoDB
    report_data = {
        "file_name": file.filename,
        "file_hash": file_hash,
        "metadata": initial_state["metadata"],
        "raw_artifacts": final_state["raw_artifacts"],
        "final_report": final_state["final_report"],
        "created_at": datetime.utcnow()
    }
    
    await db.analysis_sessions.insert_one(report_data)
    
    return AnalysisResponse(
        status="success",
        is_cached=False,
        data=AnalysisReport(**report_data)
    )
