from imageToText import ImageToText
img = ImageToText()
img.read('./img.jpg')
print(img.getText())