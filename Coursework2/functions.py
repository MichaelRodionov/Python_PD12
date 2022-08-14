import requests as r
import random
from basic_word import BasicWord


def load_random_word(file_json):
    """
    Requests JSON file from jsonkeeper, chose random word, make copy of the class BasicWord, return this copy
    """
    response = r.get(file_json)
    data = response.json()
    line = random.choice(data)
    word = BasicWord(line['word'], line['subwords'])
    return word
