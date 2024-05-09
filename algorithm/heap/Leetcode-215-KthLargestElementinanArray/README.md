## 1. 이해 
    정렬되지 않은 정수 배열에서 n번째 큰 수를 구하시오. (단, 정렬을 사용하지 않고 풀어보시오.)

## 2. 계획
* 정렬을 사용하지 않아야 하기에, __최대 힙__ 을 이용해서 풀이.  
    * 파이썬의 경우 heapq모듈이 최소 힙만 지원하기에, 적절히 변형하여 최대값을 구할 수 있음.

## 3. 풀이 (heapq 모듈 이용)
* __전체코드__  
```python
    class Solution:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            heap = []
            
            for i in nums :
                heapq.heappush(heap,-i)
            
            for _ in range(k-1):
                heapq.heappop(heap)
            
            return -heapq.heappop(heap)
```
위에서 말했듯 파이썬 heapq모듈은 최소 힙만 지원하므로, 이를 이용해서 heap에 push할 때, __음수로 변환하여 push__ 하여 __추출할 때 부호를 변환__ 하면 최대 힙처럼 작동하도록 구현.

## 3-1. 예제풀이 (heapq모듈 heapify 이용)
* __heapify()__ 는 자료구조를 힙으로 변환하는 함수.  
이 역시 최소 힙으로 변환되기에, 예를 들어 6개의 숫자 중에 2번째로 큰 수를 찾는 연산을 5번째로 작은 수를 찾는 식으로 바꾸어 구현.
```python
    for i in range(len(nums)-k) :
        heapq.heappop(nums)
```

* __전체코드__
```python
    class Solution:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            heapq.heapify(nums)

            for i in range(len(nums)-k) :
                heapq.heappop(nums)

            return heapq.heappop(nums)
```

## 3-2. 예제풀이 (heapq모듈 nlargest 이용)
* heapq 모듈에서는 k번째 큰 숫자까지 가장 큰 값부터 순서대로 리스트 형태로 리턴해주는 __nlargest()__ 함수가 존재.  
    * 내부적으로 heapify() 함수를 호출해주기 빼문에 번거롭게 따로 처리할 필요 없어 편리.

* __전체코드__
```python
    class Solution:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            return heapq.nlargest(k,nums)[-1]
```

## 3-3. 예제풀이 (정렬을 이용한 풀이)
* 문제에서 정렬을 사용하지 말라고 했지만, 가장 직관적인 풀이기에 한 번 시도해보자.

* __전체코드__
```python
    class Solution:
        def findKthLargest(self, nums: List[int], k: int) -> int:
            return sorted(nums, reverse = True)[k-1]
```
실행 결과 '정렬'방식이 가장 빠름.  
파이썬의 정렬 함수는 __Timsort__ 를 사용하여 C언어로 정교하게 구현되어 있기에, 대부분의 경우엔 파이썬 내부 함수를 사용하는 편이 성능이 제일 좋음.

## 4. 비고
* 자료구조를 heap으로 변환하기 위한 작업 : __heappush n번 시행__ VS __heapify 함수__
    * heappush는 __시간복잡도 O(log n)__ 의 작업으로 n번 시행하면 __O(nlog n)__ 의 시간이 걸림.
    * heapify 함수는 단순히 heappush를 n번 시행하여 heap으로 변환하는 것이 아닌 다른 방식으로 변환.

        ```python
            def _siftup(heap, pos):
                endpos = len(heap)
                startpos = pos
                newitem = heap[pos]
                # Bubble up the smaller child until hitting a leaf.
                childpos = 2*pos + 1    # leftmost child position
                while childpos < endpos:
                    # Set childpos to index of smaller child.
                    rightpos = childpos + 1
                    if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                        childpos = rightpos
                    # Move the smaller child up.
                    heap[pos] = heap[childpos]
                    pos = childpos
                    childpos = 2*pos + 1
                # The leaf at pos is empty now.  Put newitem there, and bubble it up
                # to its final resting place (by sifting its parents down).
                heap[pos] = newitem
                _siftdown(heap, startpos, pos)

            def heapify(x):
                """Transform list into a heap, in-place, in O(len(x)) time."""
                n = len(x)
                # Transform bottom-up.  The largest index there's any point to looking at
                # is the largest with a child index in-range, so must have 2*i + 1 < n,
                # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
                # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
                # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
                for i in reversed(range(n//2)):
                    _siftup(x, i)
        ```
        ----  
        
        실제 파이썬 heapify 함수의 형태지만, 이를 더 이해하기 쉽게 변환하면

        ```python
        def swap_for_heapify(arr, lenArr, rootIdx) :
            smallestIdx = rootIdx
            leftChildIdx = 2 * rootIdx + 1
            rightChildIdx = 2 * rootIdx + 2

            if (leftChildIdx < lenArr and arr[leftChildIdx] < arr[rootIdx]) :
                smallestIdx = leftChildIdx

            if (rightChildIdx < lenArr and arr[rightChildIdx] < arr[smallestIdx]) :
                smallestIdx = rightChildIdx


            if (smallestIdx != rootIdx) :
                    [arr[rootIdx], arr[smallestIdx]] = [arr[smallestIdx], arr[rootIdx]]
                    heapify(arr, lenArr, smallestIdx)

        def heapify(arr):
            lenArr = len(arr)
            # 마지막 부모 노드부터 시작하여 루트 노드까지 역순으로 heapify 호출
            for i in range(lenArr // 2 - 1, -1, -1):
                swap_for_heapify(arr, lenArr, i)
        ```
        위와 같은 형태로 변환 할 수 있다.

        천천히 코드를 살펴보면 
        ```python
            def swap_for_heapify(arr, lenArr, rootIdx) :
                smallestIdx = rootIdx
                leftChildIdx = 2 * rootIdx + 1
                rightChildIdx = 2 * rootIdx + 2

                if (leftChildIdx < lenArr and arr[leftChildIdx] < arr[rootIdx]) :
                    smallestIdx = leftChildIdx

                if (rightChildIdx < lenArr and arr[rightChildIdx] < arr[smallestIdx]) :
                    smallestIdx = rightChildIdx


                if (smallestIdx != rootIdx) :
                        [arr[rootIdx], arr[smallestIdx]] = [arr[smallestIdx], arr[rootIdx]]
                        heapify(arr, lenArr, smallestIdx)
        ```
        swap_for_heapify 함수는 루트노드와 자식 노드간의 값을 비교하여 더 큰 값을 가진 자식과 swap되고, swap된 노드 (원래의 부모노드)는 또 다시 그 자식 간의 heapify연산을 재귀적으로 리프노드가 나올 때까지 반복.  

        ![Alt text](https://media.geeksforgeeks.org/wp-content/uploads/20230323191740/Heapify-Operation-in-min-heap.webp)


        ```python
            def heapify(arr):
                lenArr = len(arr)
                
                for i in range(lenArr // 2 - 1, -1, -1):
                    swap_for_heapify(arr, lenArr, i)
        ```
        __swap_for_heapify__ 함수를 마지막 부모노드부터 루트노드까지 시행하여 최종적으로 최소 힙을 만들 수 있다.
    
        결론적으로 heapify의 시간복잡도를 계산해보면 __제일 밑에 있는 노드들의 swap_for_heapify 연산은 노드들이 적기에 O(1)로 아주 빠르게 수행__ 되지만, __루트 노드에 가까워 질 수록 swap_for_heapify 연산은 힙의 높이 만큼의 레벨을 거쳐야 하기에 더 많은 시간을 필요__ 로 한다.  

        정리하자면, heapify 함수는 각 레벨에 있는 노드 수와 연산의 수가 서로 상쇄되어, 전체적으로 __선형적인 시간__ 에 가까워지기에 시간복잡도는 __O(n)__ 이 된다.

    * 결론적으로, __heapify연산__ 이 더 효율적으로 heap변환이 가능하다.
    


    


