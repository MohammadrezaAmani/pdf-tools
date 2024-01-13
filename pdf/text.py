# -----------------------------Image To text-----------------------------------
# author: Mohammadreza Amani
# GitHub: https://www.github.com/MohammadrezaAmani
# Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
# Date: 2021/02/12
# ---------------------------------code----------------------------------------

import logging
import os

import pytesseract
from PIL import Image


class ImageToText:
    """
    A class for converting images to text using OCR (Optical Character Recognition).
    """

    def __init__(self, path: str = "./") -> None:
        """
        Initializes an instance of the ImageToText class.

        Args:
            path (str): The path to the directory containing the images.
        """
        logging.info("Initializing ImageToText class")
        self.path = path
        self.text = None
        self.image = None
        self._images = []
        self._texts = []

    def RGBToBW(self, name: str) -> Image:
        """
        Converts an RGB image to black and white.

        Args:
            name (str): The name of the image file.

        Returns:
            Image: The converted black and white image.
        """
        logging.info("Converting RGB image to BW")
        image_file = Image.open(name)
        image_file = image_file.convert("1")
        return image_file

    def read(self, name) -> str:
        """
        Reads the text from an image.

        Args:
            name (str): The name of the image file.

        Returns:
            str: The extracted text from the image.
        """
        logging.info("Reading image %s" % name)
        image = self.RGBToBW(name)
        text = pytesseract.image_to_string(image)
        self._texts.append(text)
        logging.info("text: %s" % text)
        return text

    def read_all(self) -> str:
        """
        Reads the text from all images in the specified directory.

        Returns:
            str: The concatenated text from all images.
        """
        logging.info("Reading all images")
        for image in os.listdir(self.path):
            name = os.path.join(self.path, image)
            self.read(name)

        return " ".join(self._texts)

    def save(self, name) -> None:
        """
        Saves the extracted text to a file.

        Args:
            name (str): The name of the output file.
        """
        logging.info("Saving text to %s" % name)
        with open(name, "w", encoding="utf-8") as file:
            for text in self._texts:
                file.write(text)

    def clear(self) -> None:
        """
        Clears all data stored in the instance.
        """
        self.text = None
        self.image = None
        self._images = []
        self._texts = []
        logging.info("Cleared all data")
