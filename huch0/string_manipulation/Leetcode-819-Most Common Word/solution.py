class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        unbanned_words = []

        # 1. Preprocess paragraph
        # 1-1. Subtract characters that are not word characters.
        # 1-2. Convert paragraph to lowercase.
        # 1-3. Split paragraph into words.
        # 1-4. Push words that are not in banned list.
        unbanned_words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                            .lower().split()
                                if word not in banned]

        # 2. Count each words.
        counts = collections.Counter(unbanned_words)

        # 3. Return most common key of counts
        # @info : most_common() method returns a list of (key,value) tuple.

        return counts.most_common(1)[0][0]