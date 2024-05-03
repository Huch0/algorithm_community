## 1. 이해 
    두 노드 간의 차이가 가장 작은 값의 차이를 출력하시오.

    입력 : root = [4,2,6,1,3,null,null]
    출력 : 1

    설명 :             4
                     /  \
                    2    6
                   / \
                  1   3
    
        노드 3과 4의 차이는 1이다. 

## 2. 계획
* BST에서 값의 차이가 가장 작게 나려면, __해당 노드보다 작은 것들(왼쪽 서브트리)중에 가장 큰 수__ 또는 __해당 노드보다 큰 것들(오른쪽 서브트리) 중에 가장 작은 수__ 이 두 개와만 비교하면 됨.

* 트리 상의 모든 노드에서 위와 같은 계산을 진행하면 되므로, __재귀__ 를 이용해서 풀이.

## 3. 풀이
* 해당 노드에서 왼쪽 자식 노드가 있을 경우, 왼쪽 서브트리에서 가장 큰 값을 찾기 위해 오른쪽 자식만 NULL값이 아닐 때까지 찾음.

* 그래서 찾은 노드의 값과 현재 노드의 값의 차와 트리 전체의 최소 차이와 비교하여 업데이트.

```python
    if root.left :
        left_compare_node = root.left
        while left_compare_node.right :
            left_compare_node = left_compare_node.right
        self.min_diff = min(self.min_diff,abs(root.val-left_compare_node.val))

```

* 오른쪽 서브트리에서도 비슷하게 가장 작은 값을 찾아 트리 전체의 최소 차이와 비교하여 업데이트.

```python
if root.right :
    right_compare_node = root.right
    while right_compare_node.left :
        right_compare_node = right_compare_node.left
    self.min_diff = min(self.min_diff,abs(root.val-right_compare_node.val))
```

* 위와 같은 계산을 트리의 모든 노드에서 동일하게 진행해야 하기 위해 __재귀__ 를 이용.
```python
    self.minDiffInBST(root.left)
    self.minDiffInBST(root.right)
```

* __전체코드__  
```python
    class Solution:
        min_diff = sys.maxsize
        def minDiffInBST(self, root: Optional[TreeNode]) -> int:
            if not root : return self.min_diff
            
            if root.left :
                left_compare_node = root.left
                while left_compare_node.right :
                    left_compare_node = left_compare_node.right
                self.min_diff = min(self.min_diff,abs(root.val-left_compare_node.val))


            if root.right :
                right_compare_node = root.right
                while right_compare_node.left :
                    right_compare_node = right_compare_node.left
                self.min_diff = min(self.min_diff,abs(root.val-right_compare_node.val))

            self.minDiffInBST(root.left)
            self.minDiffInBST(root.right)

            return self.min_diff
```

* 초기 노드 차이(min_diff)의 최솟값을 __sys.maxsize__ 으로 설정

* 노드가 NULL인 경우 min_diff를 그대로 리턴하여 사실상 아무런 계산도 하지 않은 채로 리턴.

## 3-1. 예제 코드
* 왼쪽 서브트리의 가장 큰 값과 오른쪽 서브트리의 가장 작은 값과의 비교를 이용해서 풀이하는 것은 동일.

* 중위 순회를 이용하면 BST상에서 크기 순으로 순회하기 때문에 바로 앞의 갚과 현재 노드값을 비교하면 그게 바로 가장 작은 차이임을 이용.

``` 
예시:
                               8
                              / \
                             4  12
                            / \
                           2   6
                          / \ / \
                         1  3 5  7
    
    이 트리를 중위 순회 할 경우 [1,2,3,4,5,6,7,8,12]순으로 순회.
```

* 전체코드
```python
    class Solution:
        prev = -sys.maxsize-1
        result = sys.maxsize

        def minDiffInBST(self, root: Optional[TreeNode]) -> int:
            if root.left :
                self.minDiffInBST(root.left)

            self.result = min(self.result,root.val-self.prev)
            self.prev = root.val

            if root.right:
                self.minDiffInBST(root.right)

            return self.result
```

## 4. 비고
* 일반적으로 최솟값(정수)을 구하는 문제에는 초기 최솟값 변수를 int형의 최댓값( __sys.maxsize__ )을 설정하고, 계산을 진행하며 줄여나가는 풀이가 이상적.

* 그와 비교하여 최댓값(정수)를 구하는 문제는 초기 최솟값 변수를 int형의 최솟값 ( __-sys.maxsize-1__ )을 설정하면 됨.

