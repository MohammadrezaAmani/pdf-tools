#-----------------------------Image To text-----------------------------------
# author: Mohammadreza Amani
# GitHub: https://www.github.com/MohammadrezaAmani
# Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
# Date: 2022/02/12
#---------------------------------code----------------------------------------

import pytesseract
import os
from PIL import Image

class ImageToText:
    def __init__(self, path = './'):
        self.path = path
        self.text = None
        self.image = None
        self.images = []
        self.texts = []
    def RGBToBW(self,name):
        image_file = Image.open(name)
        image_file = image_file.convert('1') 
        self.image = image_file
    def read(self,name):
        self.RGBToBW(name)
        self.text = pytesseract.image_to_string(self.image)
        self.texts.append(self.text)
    def readAll(self):
        for image in self.images:
            self.read(image)
    def save(self,name):
        with open(name, 'w') as file:
            for text in self.texts:
                file.write(text)
    def getText(self):
        return self.text
    def getTexts(self):
        return self.texts
    def setPath(self,path):
        self.path = path
    def setImages(self,images):
        self.images = images
    def getImages(self):
        return self.images
    def clear(self):
        self.text = None
        self.image = None
        self.images = []
        self.texts = []
    