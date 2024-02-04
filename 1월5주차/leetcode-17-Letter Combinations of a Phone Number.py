#nested function
class Solution:
    def letterCombinations(self, digits: str) -> List[str]: # 이렇게 생각을 많이햇는데 5분도 안지남 ..
        if len(digits) == 0:
            return []
        answer = []
        mydict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
            }
        def dfs(i, s):
            if i == len(digits):
                answer.append("".join(s))
            else:
                for c in mydict[digits[i]]:
                    s.append(c)
                    dfs(i+1, s)
                    s.pop()
        term = []
        dfs(0, term)
        return answer