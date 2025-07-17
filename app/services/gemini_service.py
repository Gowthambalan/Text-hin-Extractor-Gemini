import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def extract_text_from_image(image_bytes: bytes) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": "Extract Hindi text from this image."},
                    {"inline_data": {"mime_type": "image/jpeg", "data": image_bytes}}
                ]
            }
        ]
    )

    return response.text
