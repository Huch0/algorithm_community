## 1. 이해
   트리에서 __low <= node.val <= high__ 범위의 node의 value값들의 합을 구하시오 

## 2. 계획
   위 -> 아래로 내려가면서 범위 내에 있는 노드들의 합을 구하는데, 그 과정이 동일하기 때문에 __DFS(재귀)__ 를 사용하기로 계획.

## 3. 풀이

* __노드의 값이 범위를 넘어가는 경우 ( low보다 작거나 high보다 큰 경우 )__

     low 값보다 작으면 왼쪽 서브트리( BST에서 왼쪽은 루트보다 작기 때문)는 더이상 조사할 필요가 없음.  
     위의 경우와 반대로 high 값보다 크면 오른쪽 서브트리는 조사 할 필요가 없음.
   
   ```python
        if root.val < low : 
            self.rangeSumBST(root.right,low,high)
        elif root.val > high :
            self.rangeSumBST(root.left,low,high)
   ```

* __노드의 값이 범위 내에 있는 경우__

     일단 범위 내에 있기 때문에 노드합(sum_of_value)에 노드값을 더해준다.


     그리고 이 경우에도 low 값과 같은 경우, high 값과 같을 때는 각각 왼쪽 서브트리, 오른쪽 서브트리는 더이상 조사할 필요가 없음.  
     그 외에 low값과 high값 사이에 있는 경우에는 왼쪽,오른쪽 서브트리를 다시 조사.

   ```python
       else :
         self.sum_of_node += root.val
         if root.val == high :
             self.rangeSumBST(root.left,low,high)
         elif root.val == low :
             self.rangeSumBST(root.right,low,high)
         else :
             self.rangeSumBST(root.left,low,high)
             self.rangeSumBST(root.right,low,high)
   ```

   * __전체코드__
   ```python
      class Solution:
          sum_of_node = 0
          def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
      
              if not root : return 
      
              if root.val < low : 
                  self.rangeSumBST(root.right,low,high)
              elif root.val > high :
                  self.rangeSumBST(root.left,low,high)
              else :
                  self.sum_of_node += root.val
                  if root.val == high :
                      self.rangeSumBST(root.left,low,high)
                  elif root.val == low :
                      self.rangeSumBST(root.right,low,high)
                  else :
                      self.rangeSumBST(root.left,low,high)
                      self.rangeSumBST(root.right,low,high)
              
              return self.sum_of_node
   ```
   이 경우 불필요한 탐색을 배제하게 됨으로 탐색 효율이 높다.

### 3-1. 예제 풀이 (DFS 재귀 가지치기)

* __대략적인 풀이 방식은 비슷하지만, 결과값 변수를 따로 지정하지 않고, 함수의 return 값을 노드들의 합으로 설정__ 


     
     
   

   
   
* __전체코드__
```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node) :
            if not node : return 0

            if node.val < low : 
                return dfs(node.right)
            if node.val > high : 
                return dfs(node.left)

            return node.val + dfs(node.right) + dfs(node.left)

        return dfs(root)
```

### 3-2. 예제 풀이 (DFS 스택 이용)

* __재귀 방식을 스택을 이용한 반복으로 풀이__

    일반적인 경우에 반복을 활용한 풀이의 경우 직관적으로 이해하기 쉽다는 장점을 가짐.

* __전체코드__
```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        sum_of_node = 0

        while stack :
            node = stack.pop()

            if not node : continue

            if node.val < low : stack.append(node.right)
            elif node.val > high : stack.append(node.left)
            else : 
                sum_of_node += node.val
                stack.append(node.left)
                stack.append(node.right)
        return sum_of_node
```

### 3-3. 예제 풀이 (BFS 큐 이용)
* __BFS로 큐를 이용한 풀이__
    3-2의 풀이에서 스택을 큐로, pop()을 popleft()로 변경하기만 하면 됨.

* __전체코드__
```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = collections.deque([root])
        sum_of_node = 0

        while queue :
            node = queue.popleft()

            if not node : continue

            if node.val < low : queue.append(node.right)
            elif node.val > high : queue.append(node.left)
            else : 
                sum_of_node += node.val
                queue.append(node.left)
                queue.append(node.right)
        return sum_of_node
```

## 4. 비고
* __함수를 작성할 때, 모든 리턴값의 자료형은 동일해야 함(재귀의 경우 더욱 더 주의)__

    3-2 풀이에서 
    ```python
    if not node : return
    ...
    return node.val + dfs(node.right) + dfs(node.left)
    ```
    이런 식으로 자료형이 다를 경우 NoneType과 int형의 + 연산을 지원하지 않기 때문에 에러 발생
