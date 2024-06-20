## 1. 이해
* __특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 index를 출력하시오.__
* 입력 : ```nums = [4,5,6,7,0,1,2]```, ```target = 1```
* 출력 : ```5```

## 2. 계획
* target 값만 찾으면 되는 문제이기에 피벗을 기준으로 왼쪽 / 오른쪽으로 나눠 (정렬된 채로 탐색하기 위함) 두 번 이진탐색.

## 3. 풀이 (두 번 이진탐색)

* __값이 증가하다가 감소하는 지점이 바로 회전하기 전 첫번째 값이기에, for문을 이용하여 pivot 변수에 저장__

    ```python
    pivot = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] : 
                start = i+1
                break
    ```

* __pivot 변수를 기준으로 왼쪽 / 오른쪽은 이미 정렬된 상태기 때문에 이진 검색을 사용할 수 있다. 이걸 이용하여 이진검색으로 target값을 탐색.__

    ```python
    result = bisect.bisect_left(nums,target,left,right)
        if result < len(nums) and nums[result] == target :
            return result
        
        left = 0
        right = pivot
        result = bisect.bisect_left(nums,target,left,right)
        if result < right and nums[result] == target :
            return result
    ```

* __전체 코드__

    ```python
    import bisect

    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            pivot = 0
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1] : 
                    start = i+1
                    break

            left = pivot
            right = len(nums)
            
            result = bisect.bisect_left(nums,target,left,right)
            if result < len(nums) and nums[result] == target :
                return result
            
            left = 0
            right = pivot
            result = bisect.bisect_left(nums,target,left,right)
            if result < right and nums[result] == target :
                return result
            
            return -1
    ```

## 3-1. 예제풀이 (피벗을 기준으로 이진검색)
* __먼저 피벗을 기준으로 이진검색을 하기 위해선 피벗의 위치를 찾아야 한다.__
    ```python
    left, right = 0, len(nums)-1
    
    while left < right :
        mid = left + (right-left)//2

        if nums[mid] > nums[right] :
            left = mid + 1
        else : right = mid
    
    pivot = left
    ```
    * 이진검색을 응용하여 최솟값을 찾는 알고리즘이다.

    * ```mid값이 right값보다 큰 경우```는 오른쪽 값들 중에 피벗이 존재함을 뜻하기에 오른쪽 값들을 기준으로 다시 탐색

    * ```mid값이 right값보다 작은 경우```는 옳게 정렬 된 경우이기에 왼쪽 값들 중에 피벗이 존재함을 뜻하기에 왼쪽 값들을 기준으로 다시 탐색

    * 위의 과정을 반복하여 최종적으로 left에 피벗 index가 오도록 함.

* __이제 피벗을 기준으로 이진검색 진행__
    ```python
    left, right = 0, len(nums) - 1

    while left <= right :
        mid = left + (right-left)//2
        mid_pivot = (mid+pivot)%len(nums)
        
        if nums[mid_pivot] > target :
            right = mid - 1
        elif nums[mid_pivot] < target :
            left = mid + 1
        else : return mid_pivot
    return -1
    ```
    * 다른 부분은 일반적인 이진검색과 동일하지만,
    * ```mid_pivot = (mid+pivot)%len(nums)``` 이렇게 pivot을 기준으로 mid 값들을 돌려 줌으로써 피벗을 기준으로 이진검색을 진행할 수 있다.

* __전체코드__

    ```python
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            if not nums : return -1

            left, right = 0, len(nums)-1
            while left < right :
                mid = left + (right-left)//2

                if nums[mid] > nums[right] :
                    left = mid + 1
                else : right = mid
            
            pivot = left
            left, right = 0, len(nums) - 1
            while left <= right :
                mid = left + (right-left)//2
                mid_pivot = (mid+pivot)%len(nums)
                
                if nums[mid_pivot] > target :
                    right = mid - 1
                elif nums[mid_pivot] < target :
                    left = mid + 1
                else : return mid_pivot
            return -1
    ```