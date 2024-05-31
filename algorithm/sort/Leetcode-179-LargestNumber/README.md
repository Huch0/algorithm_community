## 1. 이해
* 다음 항목들을 조합하여 만들 수 있는 가장 큰 수를 구하시오.  
ex ) __입력__ : [10,2] / __출력__ : 210

## 2. 계획
* 기본적으로 큰 틀로 보면 항목들을 내림차순 정리하면 되는 문제다. 그런데 특수하게 '2','10' 중에 실제로 큰 수는 '10'이지만 이 문제에선 '210'과 '102'를 비교하기에 '2''10'순으로 와야한다. 즉, __일반적인 크기 비교가 아니라 이 문제의 특성에 맞는 크기 비교 함수__ 만 만들고, 정렬은 일반적으로 진행하면 문제를 해결할 수 있다.

## 3. 풀이 (삽입 정렬을 이용한 풀이)

* __이 문제 만의 특수한 크기 비교 함수__
    ```python
    def a_is_bigger_than_b(a,b) :
        char_a = str(a)
        char_b = str(b)

        if char_a[0] > char_b[0] : return True
        elif char_a[0] == char_b[0] : 
            x = int(char_a + char_b)
            y = int(char_b + char_a)
            if x > y : return True
            else : return False 
        else : return False
    ```
    * 이 문제는 숫자들끼리의 병합의 크기(1+2=12 < 2+1=21)를 비교해야 하기에, __입력받은 숫자를 문자로 바꾸어, 그 문자들끼리 합하여 병합한다__
    
    * 그 후에 병합한 두 결과를 다시 정수형으로 바꿔 크기 비교를 진행

* __일반적인 삽입정렬에서 크기 비교 부분에 작성한 크기 비교 함수만 대입__
    ```python
        key = 1

        while(key < len(nums)) :
            cur = key-1
            temp = nums[key]
            
            while(cur>0) :
                if a_is_bigger_than_b(nums[cur],temp) :
                    nums[cur+1] = temp
                    break
                else : 
                    nums[cur+1] = nums[cur]
                    cur -= 1

            if cur == 0 :
                if a_is_bigger_than_b(temp, nums[cur]):
                    nums[cur+1] = nums[cur]
                    nums[cur] = temp
                else :
                    nums[cur+1] = temp
            key += 1
    ```
    * 배열에서 key값을 하나씩 늘려가며 '배열의 key값 이전 값들(이미 정렬된 배열)'을 역순으로 비교해나가며 자기 자리를 찾아나간다.(삽입정렬)

* __마지막으로 정렬된 배열을 join함수를 이용해서 하나의 숫자로 합쳐 리턴__
    ```python
    return str(int(''.join(map(str,nums))))
    ```
    * ```00``` 같은 경우엔 ```0``` 으로 출력돼야 하기 때문에, __정렬된 배열을 병합한 결과를 다시 int -> str로 변경__ 하여 문제 해결

* __전체코드__

    ```python
    class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def a_is_bigger_than_b(a,b) :
            char_a = str(a)
            char_b = str(b)

            if char_a[0] > char_b[0] : return True
            elif char_a[0] == char_b[0] : 
                x = int(char_a + char_b)
                y = int(char_b + char_a)
                if x > y : return True
                else : return False 
            else : return False
        
        key = 1

        while(key < len(nums)) :
            cur = key-1
            temp = nums[key]
            
            while(cur>0) :
                if a_is_bigger_than_b(nums[cur],temp) :
                    nums[cur+1] = temp
                    break
                else : 
                    nums[cur+1] = nums[cur]
                    cur -= 1

            if cur == 0 :
                if a_is_bigger_than_b(temp, nums[cur]):
                    nums[cur+1] = nums[cur]
                    nums[cur] = temp
                else :
                    nums[cur+1] = temp
            key += 1
        
        return str(int(''.join(map(str,nums))))    
    ```

    