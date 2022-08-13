class Question:

    def __init__(self, text_question, difficulty, correct_answer, questions_list_json):
        self.text_question = text_question
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.user_answer = None
        self.answer_score = int(self.difficulty) * 10
        self.is_question = False
        self.questions_list_json = questions_list_json

    def is_correct(self):
        """ Return True, if user answer corresponds correct answer, or False if not """
        if self.correct_answer == self.user_answer:
            return True
        else:
            return False

    def get_points(self):
        """
        Return int, count of points.
        Points depend on difficulty: difficulty level 1  = 10 points, difficulty level 5 = 50 points.
        """
        return self.answer_score

    def build_question(self):
        """
        Return the text question, like:
        Question: What do people often call American flag?
        Difficulty 4/5
        """
        return f'\nQuestion: {self.text_question}\nDifficulty: {self.difficulty}/{len(self.questions_list_json)}'

    def get_feedback(self):
        """
        Return feedback with right answer or wrong answer
        """
        if self.is_correct():
            self.is_question = True
            return f'Right answer, you get {self.answer_score} points'
        else:
            return f'Wrong answer, the right one was {self.correct_answer}\n'

    def is_answered(self):
        """
        Return True if question is answered or False if not answered
        """
        return self.is_question

    def get_user_answer(self, user_answer):
        """
        Writes down user answer
        """
        self.user_answer = user_answer
