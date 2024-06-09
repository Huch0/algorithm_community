## 1. 이해
* __평면상의 points 목록이 있을 떄, (0,0) 에서 K번 가까운 점 목록을 순서대로 출력하시오__
    * __입력 : points[[3,3],[5,-1],[-2,4]], K=2__
    * __출력 : [[3,3],[-2,4]]__

## 2. 계획
* 각 점들에서 원점까지의 거리는 공식으로 모두 구할 수 있기에, 그 값을 기준으로 정렬하여 출력.

## 3. 풀이 ( sort()에서 key lambda 활용 )

* __sort()에서 key lambda 활용__

    ```python
    points.sort(key = lambda x : x[0]**2+x[1]**2)
    ```
    * 위의 코드처럼 sort()에서 key값으로 lambda를 활용해서 lambda의 값을 각 점에서의 원점까지의 거리로 하면 그 값을 기준으로 정렬할 수 있다.

* __전체 코드__
    
    ```python
    class Solution:
        def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            points.sort(key = lambda x : x[0]**2+x[1]**2)
            return points[:k]
    ```

## 3-1. 예제코드 (heap 이용)
* __상위 k개를 뽑는 것이기에, 그에 적합한 heap 자료구조를 사용__
* __전체 코드__
    
    ```python
    import heapq

    class Solution:
        def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            heap = []
            for point in points :
                x,y = point[0], point[1]
                distance_squared = x**2 + y**2
                heapq.heappush(heap,(distance_squared,[x,y]))
            
            result = []
            for _ in range(k) :
                result.append(heapq.heappop(heap)[1])
            return result
    ```
    * 구하는 것이 원점에서 거리가 가까운 k개의 points를 구하는 것이기에, 최소 힙에 ```(원점과의 거리,[x,y])```순으로 heappush
    * K번 heappop하여 ```[x,y]```만 추출하면 정답을 구할 수 있다.  

## 4. 비고
* __lambda 함수__
    * 람다는 다음과 같은 형태로 정의
        
        ```lambda 인자 : 표현식```
    
    람다를 활용하면 ```def```를 이용해서 함수를 정의하는 것보다 간편한 방식으로 함수를 정의할 수 있다. 예를 들어  
        
    ```python
    def add(x,y):
        return x+y
    ```
    
    다음과 같은 식을 

    ```add = lambda x,y : x+y```

    와 같이 간단하게 작성할 수 있다.

* __sort()에서 key값으로 lambda 활용__
    ```python
    List.sort(key=lambda x : len(x))
    ```
    * 위의 코드는 List의 각 요소의 길이를 기준으로 정렬

    ```python
    points.sort(key = lambda x : x[0]**2+x[1]**2)
    ```
    * 이번 문제에서는 points의 각 point들의 x,y값의 제곱 합을 기준으로 정렬하도록 할 수도 있다. (이차원 에서는 다음과 같이 활용)