class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.palindrome_ids = []
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, index, word) -> None:
        cur = self.root

        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                cur.palindrome_ids.append(index)
            cur = cur.children[char]

        cur.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        cur = self.root

        while word:
            # Discrimination #3
            if cur.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, cur.word_id])

            if not word[0] in cur.children:
                return result
            cur = cur.children[word[0]]
            word = word[1:]

        # Discrimination #1
        if cur.word_id >= 0 and cur.word_id != index:
            result.append([index, cur.word_id])

        # Discrimination #2
        for palindrome_id in cur.palindrome_ids:
            result.append([index, palindrome_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results
