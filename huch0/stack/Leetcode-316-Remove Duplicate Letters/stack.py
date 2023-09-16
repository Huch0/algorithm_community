class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []

        for char in s:
            counter[char] -= 1

            # if char is in stack, this char is already decided its position
            if char in stack:
                continue
            
            # if new character is smaller than last character in stack,
            # and if last character in stack has another element behind new character,
            # it should be removed.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(char)
        
        return ''.join(stack)
            
            