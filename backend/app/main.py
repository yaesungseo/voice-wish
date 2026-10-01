from fastapi import FastAPI
from app.routes.tts import router as tts_router

app = FastAPI()

app.include_router(tts_router)

@app.get("/")
def root():
    return {"message": "TTS server is running"}