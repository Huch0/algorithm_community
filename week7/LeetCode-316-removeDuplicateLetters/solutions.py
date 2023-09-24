from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        
        left = Counter(s)
        stack = []
        found = set()
        
        for letter in s:
            if letter in found:
                left[letter]-=1
                continue
            else:
                while stack and stack[-1]>letter and left[stack[-1]]>=1:
                    popped = stack.pop()
                    found.remove(popped)
                    
                stack.append(letter)
                left[letter] -=1
                found.add(letter)
                
        solution = ''.join(stack)
        return solution