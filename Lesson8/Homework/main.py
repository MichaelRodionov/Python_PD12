import functions as f
import random as r


def main():
    file_json = 'https://jsonkeeper.com/b/37VA'
    questions_list_json = f.get_json_file(file_json)
    questions = f.get_questions_list(questions_list_json)
    greeting = input("Hello, let's start the game. Press 'y' to start or 'n' to exit: ")

    if greeting == 'y':
        r.shuffle(questions)
        for question in questions:
            text_question = question.build_question()
            user_answer = input(f'{text_question}\nAnswer: ')
            question.get_user_answer(user_answer)
            print(question.get_feedback())
        print(f.get_stats(questions))
    else:
        print('Ok, see you later')
        exit()


if __name__ == '__main__':
    main()
