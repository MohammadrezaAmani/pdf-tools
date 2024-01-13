from pdf import PdfToImage, TextToSpeech, ImageToText

def main():
    pdf_converter = PdfToImage(path="example.pdf")
    images = pdf_converter.convert()
    pdf_converter.save(path="output_images/")

    text_converter = TextToSpeech(text="Hello, how are you?")
    text_converter.convert()
    text_converter.save(path="output_audio/speech.mp3")
    text_converter.play()

    image_converter = ImageToText(path="input_images/")
    all_text = image_converter.read_all()
    image_converter.save(name="output_text/output.txt")

if __name__ == "__main__":
    main()
