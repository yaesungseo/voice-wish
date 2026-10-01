from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.tts_service import generate_tts

router = APIRouter(prefix="/tts", tags=["tts"])

class TTSRequest(BaseModel):
    text: str
    speaker_filename: str
    language: str = "ko"

@router.post("/generate")
def tts_generate(request: TTSRequest):
    try:
        output_path = generate_tts(
            text=request.text,
            speaker_filename=request.speaker_filename,
            language=request.language
        )
        return {
            "message": "TTS generated successfully",
            "output_path": output_path
        }
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))