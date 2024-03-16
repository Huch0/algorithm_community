class Solution(object):
    def removeDuplicateLetters(self, s):
        dicCnt = {} # 해당 문자가 몇번 나왔는지 저장하는 dic
        stack = []
        
        for char in s:
            if char not in dicCnt:
                dicCnt[char] = 1
            else:
                dicCnt[char] += 1
        
        for char in s:
            dicCnt[char] -= 1
            if char in stack:
                continue
            while stack and char<stack[-1] and dicCnt[stack[-1]]>0:
                stack.pop()
            stack.append(char)
            
        return ''.join(stack)