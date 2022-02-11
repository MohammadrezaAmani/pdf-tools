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
        