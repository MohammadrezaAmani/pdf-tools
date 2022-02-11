#---------------------------pdf To image----------------------------
# author: Mohammadreza Amani
# GitHub: https://www.github.com/MohammadrezaAmani
# Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
# Date: 2021/02/12
#---------------------------------code----------------------------------------

from pdf2image import convert_from_path

class PhotoToImage:
    def __init__(self, path):
        self.path = path
        self.images = []
    def convert(self):
        self.images = convert_from_path(self.path)
        print('Converted!')
        return self.images
    def save(self, path):
        for i in range(len(self.images)):
            self.images[i].save(path + str(i) + '.jpg', 'JPEG')
        print('Done!')
    def setPath(self, path):
        self.path = path
    def getPath(self):
        return self.path
    