# 이진검색
### 이진탐색의 의미 
*   ```이진 탐색```이란 정렬된 배열에서 특정 값을 찾아내는 알고리즘이다. 어떤 값 X를 배열의 중간값과 비교한다. 만약 X가 중간값보다 크다면 배열의 우측 값들을 대상으로, 중간값보다 작다면 배열의 좌측 값들을 대상으로 위의 과정을 반복.

* 예시   
오름차순로 정렬된 배열이 있다.   
```[1,2,3,4,5,6,7]```  
이 배열에서 이진 검색을 이용해서 ```5```를 찾아보자.

    1. 
        중간값 ```4```와 ```5```를 비교한다.  
        ```4 < 5``` 이므로 ```5```는 ```4```보다 우측에 존재한다 

    2.  
        ```4``` 를 기준으로 우측에 있는 값들로 다시 탐색을 한다.  
        ```[5,6,7]```   
        중간값 ```6```과 ```5```를 비교한다.
        ```6 > 5``` 이므로 ```5```는 ```6```보다 좌측에 존재한다
    
    3. ```6```을 기준으로 좌측에 있는 값들만 남겨 놓으면,  
        ```[5]```   
        배열에 ```5```하나만 남게 되고, 그 값은 우리가 찾던 값 ```5```와 같기에 찾고 탐색을 종료한다.
    
* 종료조건   
    1. 검색에 성공할 경우 
        * 위와 같은 경우 ```배열[mid]==key```를 만족하면 탐색을 종료한다

    2. 검색에 실패한 경우
        * 더이상 탐색할 배열이 존재하지 않는 경우
        * 왼쪽의 포인터(left) > 오른쪽 포인터(right)가 될 경우 (이 경우는 문제를 풀이하며 더 자세하게 설명)
    
## 1. 이해
* __정렬된 배열을 입력받아 이진 검색으로 target에 해당하는 index를 찾으시오__

## 2. 계획
* 이진 검색은 같은 과정을 반복하는 알고리즘이기에, 재귀를 사용하기로 걔획.

## 3. 풀이 ( 재귀 )

* __sort()에서 key lambda 활용__

    ```python
    index = 0
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        
        if nums[mid] == target :
            return self.index + mid
        elif nums[mid] < target :
            self.index += mid
            return self.search(nums[mid:],target)
        else :
            return self.search(nums[:mid],target)
    ```
    * 위에서 설명했듯, target이 중간값과 같으면 탐색종료 / 작으면 좌측 값들로 탐색 다시 진행 / 크면 우측 값들로 탐색을 다시 진행하는 꼴로 말 그대로 코드를 작성

    * index값을 따로 지정하는 이유는 재귀를 할 때, 좌측값들을 탐색하는 경우엔 좌측값들의 index값과 원래 배열의 index 값이 같지만 / 우측값들을 탐색하는 경우엔 그렇지 않기에 index값을 따로 두고 우측값들을 인자로 재귀를 진행하는 경우에 index값에 이전 mid값을 더해서 진행

    * 더 자세히 설명하면 ```[1,2,3,4,5,6,7]```에서 ```6```의 index를 찾고 싶은 경우, 초기 mid의 index(```3```)에서 ```[4,5,6,7]```의 ```6```의 index(```2```)을 더하여 리턴해주어야 한다. 

* __전체 코드__
    
    ```python
    class Solution:
        index = 0
        def search(self, nums: List[int], target: int) -> int:
            if len(nums) == 0 : return -1
            if len(nums) == 1 :
                if nums[0] == target : return self.index
                else : return -1
            
            mid = len(nums)//2
            
            if nums[mid] == target :
                return self.index + mid
            elif nums[mid] < target :
                self.index += mid
                return self.search(nums[mid:],target)
            else :
                return self.search(nums[:mid],target)
    ```

## 3-1. 예제코드 (재귀)
* __위의 코드와 같은 ```재귀```를 사용하지만, index의 범위로 탐색 범위를 조절__
    ```python
    def binary_search(left:int, right:int) -> int :
    ```
    * left(low), right(high) index를 파라미터로 하는 이진 탐색 함수를 다시 작성
    
    ```python
    mid = (left+right)//2
    ```
    * 중간값의 index를 계산하고

    ```python
    if nums[mid] > target :
        return binary_search(left,mid-1)
    ```
    * 타겟이 중간값보다 작을 경우, 타겟은 중간값보다 왼쪽에 있을 거기 때문에, 탐색 범위를 ```left ~ mid-1```로 다시 탐색.

    ```python
    elif nums[mid] < target :
        return binary_search(mid+1,right)
    ```
    * 타겟이 중간값보다 클 경우, 타겟은 중간값보다 오른쪽에 있을 거기 때문에, 탐색 범위를 ```mid+1 ~ right```로 다시 탐색.

    ```python
    if left > right : return -1
    
    ...
    
    else : return mid
    ```
    1. ```중간값 == target```일 경우 탐색 종료 (중간값을 리턴) (```탐색 성공```)
    
    2. 탐색을 계속 진행하다 인자 ```left>right```가 될 경우 left와 right 사이에 탐색할 대상이 없기에 탐색 종료 (```탐색 실패```)
    
* __전체 코드__
    
    ```python
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            def binary_search(left:int, right:int) -> int :
                if left > right : return -1

                mid = (left+right)//2

                if nums[mid] > target :
                    return binary_search(left,mid-1)
                elif nums[mid] < target :
                    return binary_search(mid+1,right)
                else : return mid

            return binary_search(0,len(nums)-1)
    ```
    * 재귀를 활용하는 것은 3번 풀이와 같지만, 파라미터를 슬라이싱을 하여 사용한다는 것과 ```index 범위```를 사용한다는 것에 차이가 있다.
    * 슬라이싱을 사용하면 파라미터를 구하는데 시간복잡도는 ```O(n)```이지만 / index를 사용하면 시간복잡도는 ```O(1)```이 되기 때문에, 3-1 풀이가 더 효율적이라고 할 수 있다.

## 3-2. 예제풀이 (반복)
* __반복을 이용해서 이진 탐색 알고리즘 구현__
* __전체코드__
    ```python
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) -1
            while True :
                if left > right : return -1
                
                mid = (left+right)//2

                if nums[mid] > target :
                    right = mid-1
                elif nums[mid] < target :
                    left = mid+1
                else : return mid
    ```
    * 재귀와 거의 비슷하게, left와 right를 초기에 low index(```0```), high index(```len(nums)-1```)로 설정, 재탐색 조건, 종료 조건 모두 재귀와 동일하게 설정.

## 3-3. 예제풀이 (파이썬 이진 검색 built-in 함수 bisect)
* __파이썬에는 이미 내장된 이진 검색 모듈이 존재한다__
    ```python
    index = bisect.bisect_left(nums,target)
    ```
    * bisect_left 함수는 배열, target을 인자로 입력받고, ```target이 배열에서 들어갈 index```를 리턴한다. (nums는 정렬된 상태)

    ```python
    if index < len(nums) and nums[index] == target : return index
    else : return -1
    ```
    * 그렇기에 index가 배열의 길이 보단 작고, ```해당 index에 있는 값과 target의 값이 같다면``` ```배열 내에 target이 존재```한다는 의미와 같이 때문에, index를 리턴해주면 된다.

# 4. 비고
* __알고리즘 최적화에 있어 시간복잡도와 공간복잡도의 필요성__
    * 알고리즘에 있어 시간복잡도와 공간복잡도를 최적화하는 것은 알고리즘의 실행 속도를 높이고, 메모리 사용량을 줄이는데 기여.

    * 3번 풀이 / 3-1번 풀이 모두 재귀를 사용하지만 각각 슬라이싱(```O(n)```) / index (```O(1)```)를 사용하여 실질적으로 시간복잡도의 차이가 알고리즘 문제에 효율적인 풀이의 핵심적으로 작용한다는 것을 느낄 수 있었음.


