class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        unbanned_words = []
        unbanned_words = [word for word in re.sub(r'[^\w]', ' ', paragraph)  #정규표현식 사용
                            .lower().split()
                                if word not in banned]

        counts = collections.Counter(unbanned_words)

        return counts.most_common(1)[0][0]