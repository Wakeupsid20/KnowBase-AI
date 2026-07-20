import os
import shutil

from fastapi import APIRouter, UploadFile, File

from app.services.document_service import extract_text_from_pdf

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename,
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "pages": result["pages"],
        "characters": result["characters"],
        "preview": result["text"][:500],
    }