# class Tokenize

import re

class Tokenize:
    """ подготавливает текст для токенизаций. """
    lowertext = ""
    clearstring = ""
    onestring = ""
    def __init__(self, text):
        self.text = text

    def load(self):
        """ приводит текст в низкий регистр, замена пробелов в тесте на пустой символ, замена ё на е."""
        self.lowertext = self.text.lower()
        self.clearstring = re.sub("[\t|\n|\r|\f|\v]", "", self.lowertext)
        self.onestring = re.sub("[ё]", "е", self.clearstring)
        return self.onestring
