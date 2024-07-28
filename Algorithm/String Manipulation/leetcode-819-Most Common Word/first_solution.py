class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        print(paragraph)
        for char in "!?',;.":
            paragraph = paragraph.replace(char, ' ')
        
        words = [x for x in paragraph.split() if x not in banned]

        maxcount = 0
        most_common_word = ''

        for k in words:
            k_count = words.count(k)
            if k_count > maxcount:
                maxcount = k_count
                most_common_word = k
        
        return most_common_word
