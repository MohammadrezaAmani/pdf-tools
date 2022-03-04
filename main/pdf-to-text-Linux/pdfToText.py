import os

class PdfToText:
    def __init__(self, path='./'):
        self.path = path
        self.text = None
        self.texts = []
        self.images = []
    def toText(self):
        os.system('pdftotext -layout ' + self.path + ' -')
    def read(self):
        with open(self.path, 'r') as file:
            self.text = file.read()
            self.texts.append(self.text)
    def readAll(self):
        for image in os.listdir(self.path):
            # name of the image
            name  = os.path.join(self.path, image)
            self.read(name)
    def save(self, name):
        with open(name, 'w') as file:
            for text in self.texts:
                file.write(text)
    def toImage(self):
        os.system('pdfimages -j ' + self.path + ' ./')
    def toHtml(self):
        os.system('pdftohtml -i -c -noframes ' + self.path + ' ./')