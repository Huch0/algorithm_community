class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub("[^\w]", " ", paragraph)

        words = collections.Counter([x for x in paragraph.split() if x not in banned])

        return words.most_common()[0][0]
