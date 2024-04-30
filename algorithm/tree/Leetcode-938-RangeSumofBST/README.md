## 1. 이해
   트리에서 __low <= node.val <= high__ 범위의 node의 value값들의 합을 구하시오 

## 2. 계획
   위 -> 아래로 내려가면서 범위 내에 있는 노드들의 합을 구하는데, 그 과정이 동일하기 때문에 __재귀__ 를 사용하기로 계획.

## 3. 풀이
   
   * 노드의 값이 범위를 넘어가는 경우 ( low보다 작거나 high보다 큰 경우 )

     low 값보다 작으면 왼쪽 서브트리( BST에서 왼쪽은 루트보다 작기 때문)는 더이상 조사할 필요가 없음.
     
     위의 경우와 반대로 high 값보다 크면 오른쪽 서브트리는 조사 할 필요가 없음.
   
   ```python
        if root.val < low : 
            self.rangeSumBST(root.right,low,high)
        elif root.val > high :
            self.rangeSumBST(root.left,low,high)
   ```

   * 노드의 값이 범위 내에 있는 경우

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

   * 전체코드
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
     
     
   

   
   
