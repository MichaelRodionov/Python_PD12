class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.used_subwords_list = []

    def __repr__(self):
        return self.user_name

    def get_used_subwords_count(self):
        """
        Get count of used subwords, return int
        """
        return len(self.used_subwords_list)

    def is_used(self, user_word):
        """
        Check and  return bool if user word  in used_subword_list
        """
        return user_word in self.used_subwords_list

    def add_word_to_used_subwords(self, user_word):
        """
        Write down word into used subwords
        """
        self.used_subwords_list.append(user_word)
