# Import random library
import random as r


# List of questions, empty list for answers, dictionary
# with boolean type of answers, questions counter
words = [
    "code", "dream", "author", "program", "community",
    "information technologies", "just do it"
]
answers = []
answers_result = {
    1: True,
    2: False
}
i = 1


def morse_encode(word):
    """
    Get random word from list of words, encodes in Morse and return 
    coded word
    """
    morse_dictionary = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
    morse_word = ""
    for letter in word.replace(" ", ""):
        morse_word += morse_dictionary[letter]
    return morse_word


def get_word():
    """
    Chooses random word from list of words and return this word
    to function morse_encode
    """
    word = r.choice(words)
    return word


def print_statistics(answers):
    """
    Get list of answers, counts general amount of questions, 
    amount of correct answers, amount of incorret answers
    and print the result on the screen
    """
    total_questions = len(answers)
    right_answers = answers.count(True)
    wrong_answers = answers.count(False)
    result = f"""Amount of questions: {total_questions}
Correct answers: {right_answers}
Incorrect answers: {wrong_answers}"""
    return result


# Main code
introduction = input("""Today we will practice to decode Morse words.
Click Enter and lets begin \n""")
while i < 6:
    word_from_words = get_word()
    encoded_word = morse_encode(word_from_words)
    answer = input(f"""Word {i}: {encoded_word}
Enter encoded word: """)
    if answer == word_from_words:
        print(f"Correct, {word_from_words}!\n")
        answers.append(answers_result[1])
        i += 1
    else:
        print(f"Incorrect, {word_from_words}!\n")
        answers.append(answers_result[2])
        i += 1
    words.remove(word_from_words)

conclusion = print_statistics(answers)
print(conclusion)
