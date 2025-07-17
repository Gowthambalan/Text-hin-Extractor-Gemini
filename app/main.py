from fastapi import FastAPI
from app.routes.extract import router as extract_router

app = FastAPI(title="Hindi Text Extractor using Gemini")

app.include_router(extract_router)
