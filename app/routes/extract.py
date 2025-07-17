from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.gemini_service import extract_text_from_image

router = APIRouter()

@router.post("/extract-hindi-text/")
async def extract_hindi_text(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise HTTPException(status_code=400, detail="Only .jpg, .jpeg, .png allowed.")

    try:
        image_bytes = await file.read()
        text = extract_text_from_image(image_bytes)
        return {"extracted_text": text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
