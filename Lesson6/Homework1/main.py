import functions as f


def main():
    """ Main function """
    doc_words = "words.txt"
    doc_history = "history.txt"
    user_name = input("Enter your name: ")
    print(f"Hello {user_name}, let's start the game!")

    list_words = f.get_words(doc_words)
    counter = 0

    for word in list_words:
        coded_word = f.get_shuffle_words(word)

        user_answer = input(f"Guess the word: {coded_word}\nEnter encoded word: ")

        if user_answer == word:
            counter += 10
            print(f"Good job, it's a {word}! You get 10 points!")
        else:
            print(f"Wrong! Correct answer: {word}")

    f.get_history(doc_history, user_name, counter)

    total_games, scores = f.get_top_players(doc_history)
    record = 0

    for players in scores:
        player = players.strip().split()

        if int(player[1]) > record:
            record = int(player[1])

    print(f"Total games: {total_games}\nRecord: {record}")

if __name__ == "__main__":
    main()
