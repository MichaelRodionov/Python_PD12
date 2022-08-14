import functions as f
from player import Player


def main():
    file_json = 'https://jsonkeeper.com/b/2U37'
    stop_words = ['stop', 'стоп']
    random_word = f.load_random_word(file_json)

    user_name = input("Enter player's name: ")
    player = Player(user_name)
    print(f'Hello, {player}!\n'
          f'Make {random_word.get_subwords_count()} words from word {random_word.original_word.upper()}\n'
          f'Words must not be shorter then 3 letters\n'
          f'To end the game, guess all words or write down "stop/стоп"\n'
          f'Lets start, your first word? ')

    while len(player.used_subwords_list) < random_word.get_subwords_count():
        user_word = input().lower()

        if user_word not in stop_words:

            if len(user_word) < 3:
                print('Too short word, try another one')
            elif not random_word.is_valid(user_word):
                print('You cannot use this word, try another one')
            elif player.is_used(user_word):
                print('This word has already been used, try another one')
            else:
                print('Good word!')
                player.add_word_to_used_subwords(user_word)

        else:
            print(f'Game over, you guessed {player.get_used_subwords_count()} words from '
                  f'{random_word.get_subwords_count()}')
            exit()


if __name__ == '__main__':
    main()
