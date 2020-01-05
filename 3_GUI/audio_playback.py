# This class handles the audio playback from selected letters.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.

import simpleaudio as sa

class MyAudioClass:

    directoriesAudioFiles = {
        "c": "audio/en/c.wav",
        "v": "audio/en/v.wav",
        "l": "audio/en/l.wav",
        "g": "audio/en/g.wav"
    }

    audioFiles = {}
    play_obj = None
    mute = False

    def __init__(self):
        self.loadAudio()

    def loadAudio(self):
        for i in self.directoriesAudioFiles:
            self.audioFiles[i[0]] = sa.WaveObject.from_wave_file(self.directoriesAudioFiles[i])

    def playAudio(self, letter):
        if self.isPlaying() == False and self.mute == False:
            self.play_obj = self.audioFiles[letter].play()

    def toggleMute(self):
        if self.mute:
            self.mute = False
        else:
            self.mute = True

    def isPlaying(self):
        ret = False
        if self.play_obj != None:
            ret = self.play_obj.is_playing()
        return ret

    def isMuted(self):
        return self.mute