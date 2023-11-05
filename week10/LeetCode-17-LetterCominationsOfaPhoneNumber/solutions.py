from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        digits = [int(d) for d in digits]
        result = deque([""])
        
        for digit in digits:
            for _ in range(len(result)):
                curr = result.popleft()
                result.extend(curr + letter for letter in options[digit])
        
        return list(result)
