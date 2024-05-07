## 1. 이해 
    입력값 : 전위순회, 중위순회 결과(배열)가 나오는 최종 트리를 만들어 리턴하라

## 2. 계획
* 해당 문제를 풀기 위해선 전위순회와, 중위순회 간의 관계를 파악할 필요가 있음.

    * __전위(N,L,R) : [1, 2, 4, 5, 3, 6, 7, 9, 8]__  
    __중위(L,N,R) : [4, 2, 5, 1, 7, 9, 6, 8, 3]__
    
    * 전위에서 제일 처음 노드(1)은 루트 노드를 의미하기에, 중위에서 노드(1)을 기준으로 __왼쪽 노드들은 왼쪽 서브트리__ / __오른쪽 노드들은 오른쪽 서브트리__ 를 의미.  

        중위 : [ <span style="color:orange">4, 2, 5</span>, __1__, <span style="color:pink">7, 9, 6, 8, 3</span>] 

    * 위의 계산을 왼쪽 서브트리, 오른쪽 서브트리 각각을 또 인자로 갖는 함수를 __재귀__ 로 시행하면, 아래 -> 위로 서브트리가 만들어지며 전체 트리를 완성할 수 있음.

## 3. 풀이
* 전위의 제일 처음 노드를 루트노드로 설정

```python
    tree = TreeNode(preorder.pop(0))
```

* 중위에서 로트노드의 index 찾기

```python
    root_index = inorder.index(tree.val)
```

* 위에서 구한 루트노드의 index를 기준으로 왼쪽 노드들 / 오른쪽 노드들을 각각 인자로 갖는 왼쪽 서브트리 / 오른쪽 서브트리를 __재귀__ 를 이용해서 만듦.
```python
    tree.left = self.buildTree(preorder[:root_index], inorder[:root_index])
            tree.right = self.buildTree(preorder[root_index:], inorder[root_index+1:])
```

* __전체코드__  
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder and inorder :
            tree = TreeNode(preorder.pop(0))
            
            root_index = inorder.index(tree.val)

            tree.left = self.buildTree(preorder[:root_index], inorder[:root_index])
            tree.right = self.buildTree(preorder[root_index:], inorder[root_index+1:])

            return tree
```

## 4. 비고
* 파이썬에서 리스트의 __pop()__ 연산은 인덱스를 별도로 지정할 수 있어서, __pop(0)__ 과 같은 연산을 통해 스택, 큐의 모든 역할을 수행할 수 있다. __하지만 파이썬의 리스트에서 pop(0)의 연산은 시간 복잡도가 O(n)이기에 시간 복잡도를 줄이기 위해선 파이썬의 deque와 같은 자료형을 이용하면 된다.__

