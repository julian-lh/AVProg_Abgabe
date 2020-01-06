# This script creates a mp3 audio file from a string.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.

# need gTTS and mpg123
# pip install gTTS
# apt install mpg123

from gtts import gTTS

s = "Text"
file = "audio/de/audio.mp3"


tts = gTTS(s, 'de')
tts.save(file)



