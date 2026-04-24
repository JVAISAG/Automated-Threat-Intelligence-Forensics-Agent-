import hashlib
import os
import aiofiles
from fastapi import UploadFile
from ..core.config import settings

class FileService:
    @staticmethod
    async def get_sha256(file_path: str) -> str:
        sha256_hash = hashlib.sha256()
        async with aiofiles.open(file_path, "rb") as f:
            while chunk := await f.read(8192):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

    @staticmethod
    async def save_upload(upload_file: UploadFile) -> str:
        if not os.path.exists(settings.UPLOAD_DIR):
            os.makedirs(settings.UPLOAD_DIR)
        
        file_path = os.path.join(settings.UPLOAD_DIR, upload_file.filename)
        async with aiofiles.open(file_path, "wb") as out_file:
            while content := await upload_file.read(8192):
                await out_file.write(content)
        
        return file_path
