_Honestly, this is a simple project for 2020-2021, and the only reason I wrote it was because I didn't feel like reading books, and the books were images and not text (couldn't be converted to text with pdftotext)
Don't be harsh because the code is not pretty and was written by a lazy person._

# PDF

A Python module for handling PDFs, including features for converting PDFs to images, converting text to speech, and extracting text from images.

## PDF To Image

### Overview
The `PdfToImage` class converts PDF files to images using the `pdf2image` library.

### Example
```python
from pdf import PdfToImage

pdf_converter = PdfToImage(path="example.pdf")
images = pdf_converter.convert()
pdf_converter.save(path="output_images/")
```

## Text To Speech

### Overview
The `TextToSpeech` class converts text to speech and saves it as an audio file using `gtts` and `playsound`.

### Example
```python
from pdf import TextToSpeech

text_converter = TextToSpeech(text="Hello, how are you?")
text_converter.convert()
text_converter.save(path="output_audio/speech.mp3")
text_converter.play()
```

## Image To Text

### Overview
The `ImageToText` class extracts text from images using Optical Character Recognition (OCR) with `pytesseract`.

### Example
```python
from pdf import ImageToText

image_converter = ImageToText(path="input_images/")
all_text = image_converter.read_all()
image_converter.save(name="output_text/output.txt")
```

## Installation
To install the required dependencies, run:

```bash
pip install -r requirements.txt
```
