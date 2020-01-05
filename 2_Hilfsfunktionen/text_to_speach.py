# need gTTS and mpg123
# pip install gTTS
# apt install mpg123

from gtts import gTTS

s = ""
file = "audio/de/audio.mp3"


tts = gTTS(s, 'de')
tts.save(file)



