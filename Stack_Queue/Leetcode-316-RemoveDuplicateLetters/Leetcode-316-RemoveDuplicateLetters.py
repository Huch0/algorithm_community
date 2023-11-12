def removeDuplicateLetters(self, s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(suffix) == set(s):
            return char + self.removeDuplicateLetters(suffix.replace(char, ''))
    return ''
#recalsive


# def removeDuplicateLetters(self, s):
#     counter, seen, stack = collections.Counter(s), set(), []
#     for char in s:
#         counter[char] -= 1
#         if char in seen:
#             continue
#         while stack and char < stack[-1] and counter[stack[-1]] > 0:
#             seen.remove(stack.pop())
#         stack.append(char)
#         seen.add(char)
    
#     return ''.join(stack)
#using stack