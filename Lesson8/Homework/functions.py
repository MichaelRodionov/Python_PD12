import requests as r
import classes as c


def get_json_file(file_json):
    """
    Requests JSON file from jsonkeeper, return json file
    """
    response = r.get(file_json)
    file = response.json()
    return file


def get_questions_list(questions_list_json):
    """
    Transfer data from json file to class Question, return list of questions
    """
    questions = []
    for question in questions_list_json:
        questions.append(c.Question(question['q'], question['d'], question['a'], questions_list_json))
    return questions


def get_stats(questions):
    """
    Forms statistics of all game, like:
    That's all!
    Answered 3 out of 5 questions
    Score: 40
    """
    questions_count = len(questions)
    counter_right_answer = 0
    counter_points = 0
    for question in questions:
        if question.is_answered():
            counter_right_answer += 1
            counter_points += question.answer_score

    return f"\nThat's all!\nAnswered {counter_right_answer} out of {questions_count}\nScore: {counter_points}"
