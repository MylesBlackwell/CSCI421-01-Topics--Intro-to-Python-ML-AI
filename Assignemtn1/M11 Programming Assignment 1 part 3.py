from gtts import gTTS
import os 
import whisper


tts = gTTS("This is a test for text-to-speech and speech-to-text.", lang="en")
tts.save("test_output.mp3")

model = whisper.load_model("base")

result = model.transcribe("test_output.mp3", fp16=False)
print("Reconstructed Text:", result["text"])