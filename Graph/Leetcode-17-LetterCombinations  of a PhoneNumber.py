class Solution(object):
    def letterCombinations(self, digits):
        digitToChar = {"2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        result = []
        def dfs(i,cur):
            if len(cur)==len(digits):
                result.append(cur)
                return
            for c in digitToChar[digits[i]]:
                dfs(i+1,cur+c)
        if digits:
            dfs(0,"")
        return results