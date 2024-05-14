## 1. 이해
    트라이 자료구조를 직접 구현하시오 (insert, search, startsWith 메소드를 구현)

## 2. 계획
   기본적으로 트리구조를 기반으로 하고, 자식 노드가 여러 개인 __다진 트리__ 구조 이기 때문에, __딕셔너리__ 를 이용해서 구현.

## 3. 풀이

* __구현 상의 편리함을 위해 저장할 노드를 별도에 클래스에 구현__
    ```python
        class TrieNode:
            def __init__(self):
                self.word = False
                self.children = collections.defaultdict(TrieNode)
    ```

* __삽입 메소드__ 
    ```python
        class Trie:
            def __init__(self):
                self.root = TrieNode()
            
            def insert(self, word: str) -> None:
                node = self.root
                for char in word :
                    node = node.children[char]
                node.word = True
    ```

    삽입 시에 루트부터 자식 노드가 점점 깊어지면서, 다진 트리의 형태가 된다.

    ```python
        t = Trie()
        t.insert('apple')
        t.insert('appear')
    ```
    위의 코드로 삽입을 할 경우 

                a (word:False)
               /
              p (False)
             /
            p (False)
           /         \
          l (False)   e (False)
         /             \
        e (True)        a (False)
                         \
                          r (True)
    
    의 꼴로 저장되게 된다.

* __search 메소드__
    ```python
        def search(self, word: str) -> bool:
            node = self.root
            for char in word :
                if char not in node.children : return False
                else :
                    node = node.children[char]
            
            return node.word
    ```
    search 메소드의 경우에는 word의 각 문자를 읽으며 루트부터 내려가며 비교하는데, 다를 경우엔 바로 False를 반환한다. 그리고 word의 끝까지 같더라도, __node.word의 여부가 False인 경우엔 그 단어는 등록되지 않았기 때문에 False를 반환__ 한다. (예를 들어 'apple'이 삽입되어 있을 떄, 'app'을 search할 경우 word의 끝까지 순회가 가능하나 'app'은 word로 등록돼있지 않기 때문에 False를 반환)

* __startsWith 메소드__
    ```python
        def startsWith(self, prefix: str) -> bool:
            node = self.root
            for char in prefix :
                if char not in node.children : return False
                else : node = node.children[char]
            
            return True
    ```
    search 메소드와 거의 동일하나, __word(prefix)를 끝까지 순회하며 노드의 자식 여부만 판별__ 하여, True를 반환한다.

* __전체코드__
    ```python
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
            
            return True
    ```