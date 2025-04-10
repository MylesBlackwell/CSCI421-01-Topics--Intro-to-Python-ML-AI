from gtts import gTTS
import os 
with open("imput.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Convert Text to speech
print(text)
tts = gTTS(text, lang="fr")
tts.save("output.mp3")

os.system("start output.mp3")

print("finished")