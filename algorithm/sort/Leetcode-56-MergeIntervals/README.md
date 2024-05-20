## 1. 이해
* 문제에서 주어진 범위 중 겹치는 구간을 병합하시오  
  
  입력 : [ [1,3], [2,6], [9,10], [15,18] ]  
  출력 : [ [1,6], [8,10], [15,18]]  

  설명 : [1,3] 과 [2,6]의 범위 가 겹치기 때문에 [1,6]이 된다

## 2. 계획
* 일단 이 문제를 해결하기 위해 첫 번째 값을 기준으로 정렬을 한다.

* 정렬된 리스트를 순회하며 현재 아이템의 끝이 다음 아이템의 시작과 겹치면 병합하는 방식으로 해결해보자.

## 3. 풀이

* __2차원 배열의 첫번째 값을 기준으로 내림차순 정렬__
    ```python
    intervals.sort(key=lambda x: x[0],reverse=True)
    ```
    리스트의 __pop()연산 (시간복잡도 : O(1))__ 을 사용하기 위해 intervals을 첫번째 값을 기준으로 내림차순 정렬    
  
* __내림차순 정렬된 intervals를 뒤에서부터 순회하며 두 개의 범위가 겹치면 병합 후  pop()하여 result에 삽입__

    ```python
    level = len(intervals)-1

    result = []

    while level != 0 :
        if  intervals[level][1] >= intervals[level-1][0] :
            intervals[level-1][0] = min(intervals[level-1][0],intervals[level][0])
            intervals[level-1][1] = max(intervals[level-1][1],intervals[level][1])
            intervals.pop()
        else : result.append(intervals.pop())
        level -= 1
    result.append(intervals.pop())
    ```

* __전체코드__
    ```python
    class Solution:
        def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort(key=lambda x: x[0],reverse=True)
            level = len(intervals)-1

            result = []

            while level != 0 :
                if  intervals[level][1] >= intervals[level-1][0] :
                    intervals[level-1][0] = min(intervals[level-1][0],intervals[level][0])
                    intervals[level-1][1] = max(intervals[level-1][1],intervals[level][1])
                    intervals.pop()
                else : result.append(intervals.pop())
                level -= 1
            result.append(intervals.pop())
            return result
    ```

## 4. 비고
* __2차원 배열에서 특정 값을 기준으로 정렬하는 법__

    * __행(첫번째 값) 기준으로 정렬(오름차순)__
        ```python
        arr = [[2,3],[1,2],[0,4]]

        arr.sort(key=lambda x:x[0])

        print(arr)
        # [[0, 4], [1, 2], [2, 3]]
        ```

    * __행(첫번째 값) 기준으로 정렬(내림차순)__
        ```python
        arr = [[2,3],[1,2],[0,4]]

        arr.sort(key=lambda x: -x[0])

        print(arr)
        # [[0, 4], [1, 2], [2, 3]]
        ```

    * __열(두번째 값) 기준으로 정렬(오름차순)__
        ```python
        arr = [[2,3],[1,2],[0,4]]

        arr.sort(key=lambda x:x[1])

        print(arr)
        # [[1, 2], [2, 3], [0, 4]]
        ```
    
    * __두 번째 값이 같을 경우 첫 번째 값을 기준으로 오름차순 정렬__
        ```python
        arr = [[2, 3], [1, 2], [0, 4], [2, 2]]

        arr.sort(key=lambda x: (x[1], x[0]))

        print(arr)
        # [[1, 2], [2, 2], [2, 3], [0, 4]]
        ```
    코드 출처 : <https://asxpyn.tistory.com/75>

    
