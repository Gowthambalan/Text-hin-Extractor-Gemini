# Text-Extractor-Gemini


🧠 For example: Hindi Text Extractor using Gemini API (FastAPI)
This project is a lightweight API service built with FastAPI that extracts Hindi text from images (printed or handwritten) using the Google Gemini 1.5 Flash Vision API.

It securely handles your Gemini API key using .env, supports image uploads via REST endpoints, and returns the extracted Hindi content as structured text.


🚀 Features
🔍 Hindi OCR via Gemini: Extract Hindi text from .jpg, .jpeg, or .png images using the latest Gemini Vision API (gemini-1.5-flash)

🛡️ Environment-secured API key: Your API key is managed via .env and excluded via .gitignore

⚡ FastAPI backend: Lightweight, asynchronous Python API server

🧪 Swagger UI: Test and upload images directly through /docs (auto-generated UI)

🔒 Robust file handling: Rejects unsupported file types, prevents crashes
