from static.modules.module import *
import speech_recognition as sr


class Voicinger(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        # self.config = json.load(open(self.path_helper("config.json"), "r"))

    def test_mic(self):
        # https://realpython.com/python-speech-recognition/#working-with-microphones
        mic = sr.Microphone()
        r = sr.Recognizer()

        with mic as source:
            audio = r.listen(source)
            r.recognize_google(audio)



