#---------------------------text To speech----------------------------
# author: Mohammadreza Amani
# GitHub: https://www.github.com/MohammadrezaAmani
# Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
# Date: 2022/02/12
#---------------------------------logic----------------------------------------

import gtts
import playsound


class TextToSpeech:
    def __init__(self, text, language='en'):
        self.text = text
        self.language = language
        self.speech = None
        self.name = 'speech.mp3'

    def convert(self):
        self.speech = gtts.gTTS(self.text, self.language)
        print('Converted!')

    def save(self, path):
        self.speech.save(path)
        self.name = path
        print('Done!')

    def play(self):
        playsound.playsound(self.speech.save(self.name))
        print('Done!')

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def setLanguage(self, language):
        self.language = language

    def getLanguage(self):
        return self.language

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
