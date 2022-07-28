import random as r


def get_words(doc_words):
    """ Reads the file 'words.txt' """
    with open(doc_words, "r", encoding="utf-8") as file_words:
        content_words = file_words.read().strip().split()
        return content_words


def get_history(doc_history, name, count):
    """ Writes data in the file 'history.txt'"""
    with open(doc_history, "a", encoding="utf-8") as file_history:
        file_history.write(f"{name} {count}\n")


def get_top_players(doc_history):
    """ Read data from file 'history.txt' """
    with open(doc_history) as top_players:
        text = top_players.readlines()
        games = len(text)
        return games, text


def get_shuffle_words(word):
    """ Shuffle the letters in word """
    list_word = list(word)
    r.shuffle(list_word)
    return "".join(list_word)
