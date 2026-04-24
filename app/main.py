from fastapi import FastAPI
from .api.v1.endpoints import forensics
from .core.database import connect_to_mongo, close_mongo_connection
from .core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(forensics.router, prefix=f"{settings.API_V1_STR}/forensics", tags=["Forensics"])

@app.get("/")
async def root():
    return {"message": "Welcome to ATIF Agent API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
