import collections

class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_pailndrome(s: str) -> bool:
        return s == s[::-1]

    def insert(self, word: str, id: int) -> None:
        node = self.root
        for i, char in enumerate(word):
            if self.is_pailndrome(word[i:]):
                node.palindrome_word_ids.append(id)
            node = node.children[char]
        node.word_id = id

    def search(self, word: str, id: int) -> list[list[int]]:
        result = []

        node = self.root
        while word:
            if node.word_id >= 0:
                if self.is_pailndrome(word):
                    result.append([id, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != id:
            result.append([id, node.word_id])
            return result
        
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([id, palindrome_word_id])
            return result

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        # TLE (Time Limit Exceeded) Solution
        # def is_pailndrome(s: str) -> bool:
        #     return s == s[::-1]
        
        # outputs = []

        # for i in range(len(words)):
        #     for j in range(len(words)):
        #         if i == j:
        #             continue
        #         if is_pailndrome(words[i] + words[j]):
        #             outputs.append([i, j])
        
        # return outputs
        palindrome_ids = [i for i in range(len(words)) if words[i] == words[i][::-1] and words[i] != ""]
       
        empty_id = 5001

        if "" in words:
            empty_id = words.index("")
            words.pop(empty_id)

        reversed_words = [word[::-1] for word in words]
        tree = Trie()

        for i in range(len(words)):
            if i >= empty_id:
                tree.insert(reversed_words[i], i + 1)
            else:
                tree.insert(reversed_words[i], i)
        
        outputs = []

        for i in range(len(words)):
            if i >= empty_id:
                output = tree.search(words[i], i+1)
            else:
                output = tree.search(words[i], i)
            if output:
                outputs += output

        if empty_id < 5001:
            for palindrome_id in palindrome_ids:
                outputs.append([empty_id, palindrome_id])
                outputs.append([palindrome_id, empty_id])
        return outputs