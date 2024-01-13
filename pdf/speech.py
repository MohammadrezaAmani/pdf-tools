# ---------------------------text To speech----------------------------
# author: Mohammadreza Amani
# GitHub: https://www.github.com/MohammadrezaAmani
# Linkedin: https://www.linkedin.com/in/mohammadreza-amani/
# Date: 2021/02/12
# ---------------------------------logic----------------------------------------

import logging

import gtts
import playsound


class TextToSpeech:
    """
    A class for converting text to speech and saving it as an audio file.

    Args:
        text (str): The text to convert to speech.
        language (str, optional): The language of the text (default is "en").
        file_name (str, optional): The name of the output audio file (default is "speech.mp3").

    Attributes:
        text (str): The text to convert to speech.
        language (str): The language of the text.
        _speech (gtts.gTTS): The gTTS object representing the converted speech.
        _name (str): The name of the output audio file.

    Methods:
        convert(): Converts the text to speech using gTTS.
        save(path: str) -> bool: Saves the speech as an audio file at the specified path.
        play(): Plays the saved speech using playsound.
    """

    def __init__(
        self, text: str, language: str = "en", file_name: str = "speech.mp3"
    ) -> None:
        logging.info("Initializing TextToSpeech class")
        self.text = text
        self.language = language
        self._speech = None
        self._name = file_name

    def convert(self) -> gtts.gTTS:
        """
        Converts the text to speech using gTTS.

        Returns:
            gtts.gTTS: The gTTS object representing the converted speech.
        """
        logging.info("Converting text to speech")
        self._speech = gtts.gTTS(self.text, self.language)
        return self._speech

    def save(self, path: str) -> bool:
        """
        Saves the speech as an audio file at the specified path.

        Args:
            path (str): The path to save the audio file.

        Returns:
            bool: True if the speech is successfully saved, False otherwise.
        """
        logging.info("Saving speech to %s" % path)
        try:
            self._speech.save(path)
            self._name = path
        except Exception as err:
            logging.error(err)
            return False
        return True

    def play(self) -> None:
        """
        Plays the saved speech using playsound.
        """
        logging.info("Playing speech")
        playsound.playsound(self._name)
