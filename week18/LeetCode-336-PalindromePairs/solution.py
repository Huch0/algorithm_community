class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
        self.idx = -1
        self.palindromeIdxs = list()

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = list()
        
        for i in range(len(words)):
            cur = self.root
            rWord = words[i][::-1]
            for j in range(len(rWord)):
                if self.isPalindrome(rWord[j:]):
                    cur.palindromeIdxs.append(i)
                    
                if rWord[j] not in cur.children:
                    cur.children[rWord[j]] = TrieNode()
                cur = cur.children[rWord[j]]
                
            cur.end = True
            cur.idx = i
            
        for i in range(len(words)):
            self.search(words[i], i, res)
            
        return res
        
    def search(self, word, idx, res):   
        cur = self.root
        for i in range(len(word)):
            if cur.end and self.isPalindrome(word[i:]):
                res.append([idx, cur.idx])
                
            if word[i] not in cur.children:
                return
            cur = cur.children[word[i]]        
        
        if cur.end and cur.idx != idx:
            res.append([cur.idx, idx])
        
        for pIdx in cur.palindromeIdxs:
            res.append([idx, pIdx])
                
        return
        
        
    def isPalindrome(self, s):
        return s == s[::-1]