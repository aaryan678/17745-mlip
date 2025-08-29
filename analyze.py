from google import genai
from google.genai import types
import os
from dotenv import load_dotenv


load_dotenv()

gemini_api_key = os.getenv("gemini_api_key")
gemini_client = genai.Client(api_key=gemini_api_key)

def get_llm_response(image_bytes: bytes, mime_type="image/jpeg") -> str:
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type,
            ),
            "Caption this image."
        ]
    )
    return response.text