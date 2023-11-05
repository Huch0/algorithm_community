class Solution:    
    def letterCombinations(self, digits: str) -> list[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in dict[digits[i]]:
                    dfs(i + 1, path + j)
   
        dict = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        if not digits:
            return []
        
        result = []
        dfs(0, "")

        return result