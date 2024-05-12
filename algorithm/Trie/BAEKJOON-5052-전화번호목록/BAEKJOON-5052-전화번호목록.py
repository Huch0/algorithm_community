import collections
import sys

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)
class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word :
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word :
            if char not in node.children : return False
            else :
                node = node.children[char]
        
        return node.word


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix :
            if char not in node.children : return False
            else : node = node.children[char]
        
        return node.children
    
    
n = int(input())
for _ in range(n):
    k = int(sys.stdin.readline())
    
    List=[]
    trie= Trie()
    
    for __ in range(k):
        call_num = sys.stdin.readline().strip()
        List.append(call_num)
        trie.insert(call_num)
    
    result = "YES"
    for i in List:
        if trie.startsWith(i) : 
            result = "NO"
            break
    
    print(result)