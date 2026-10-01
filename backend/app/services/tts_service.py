import os
from TTS.api import TTS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOICES_DIR = os.path.join(BASE_DIR, "voices")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(VOICES_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

def generate_tts(text: str, speaker_filename: str, language: str = "ko") -> str:
    speaker_path = os.path.join(VOICES_DIR, speaker_filename)
    output_path = os.path.join(OUTPUTS_DIR, "cloned.wav")

    if not os.path.exists(speaker_path):
        raise FileNotFoundError(f"Speaker file not found: {speaker_path}")

    tts_model.tts_to_file(
        text=text,
        speaker_wav=speaker_path,
        language=language,
        file_path=output_path
    )

    return output_path