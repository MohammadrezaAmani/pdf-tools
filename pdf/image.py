# ---------------------------pdf To image----------------------------
# author: Mohammadreza Amani
# GitHub: https://www.github.com/MohammadrezaAmani
# Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
# Date: 2021/02/12
# ---------------------------------code------------------------------

import logging

from pdf2image import convert_from_path


class PdfToImage:
    """
    A class for converting PDF files to images.

    Args:
        path (str): The path to the PDF file. Defaults to "./".

    Attributes:
        path (str): The path to the PDF file.
        _images (list): A list to store the converted images.

    Methods:
        convert: Converts the PDF file to images.
        save: Saves the converted images to the specified path.
    """

    def __init__(self, path: str = "./"):
        """
        Initializes the PdfToImage class.

        Args:
            path (str): The path to the PDF file. Defaults to "./".
        """
        logging.info("Initializing PdfToImage class")
        self._images = []
        self.path = path

    def convert(self):
        """
        Converts the PDF file to images.

        Returns:
            list: A list of converted images.
        """
        logging.info("Converting pdf to images")
        self._images = convert_from_path(self.path)
        return self._images

    def save(self, path):
        """
        Saves the converted images to the specified path.

        Args:
            path (str): The path to save the images.
        """
        logging.info("Saving images to %s" % path)
        for i in range(len(self._images)):
            self._images[i].save(path + str(i) + ".jpg", "JPEG")
        print("Done!")
