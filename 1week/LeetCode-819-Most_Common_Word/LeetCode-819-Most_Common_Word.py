import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = re.sub(r'[^\w]', ' ', paragraph)
        words = paragraph.lower().split()
        dict_words = {}

        for word in words:
            if word not in dict_words:
                dict_words[word] = 1
            else:
                dict_words[word] += 1

        for key in dict_words:
            if key in banned:
                dict_words[key] = 0
        
        return max(dict_words, key=dict_words.get)