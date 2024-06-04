## 1. 이해
* __t가 s의 애너그램인지 판별하시오__ (애너그램 : 어떠한 단어의 문자를 재배열하여 다른 뜻을 가지는 다른 단어로 바꾸는 것)
ex ) __입력__ : s = "anagram"  t = "nagaram" / __출력__ : ture

## 2. 계획
* 애너그램 여부를 판별하기 위해선 s와 t를 모두 정렬하여 그 상태가 일치하는지 판별하면 되는 아주 간단한 문제.

## 3. 풀이 (삽입 정렬을 이용한 풀이)

* __전체코드__

    ```python
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            return sorted(s) == sorted(t)
    ```

    