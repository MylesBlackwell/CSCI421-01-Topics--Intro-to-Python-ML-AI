import whisper

model = whisper.load_model("base")

result = model.transcribe("recording3.wav", fp16=False)
print("Transcribed Text:", result["text"])