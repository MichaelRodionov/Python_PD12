class BasicWord:
    def __init__(self, original_word, valid_subwords_list):
        self.original_word = original_word
        self.valid_subwords_list = valid_subwords_list

    def __repr__(self):
        return self.original_word

    def is_valid(self, user_word):
        """
        Check user_word in valid_subword_list, return bool
        """
        return user_word in self.valid_subwords_list

    def get_subwords_count(self):
        """
        Count subwords in valid_subword_list, return int
        """
        user_subwords_count = len(self.valid_subwords_list)
        return int(user_subwords_count)
      
