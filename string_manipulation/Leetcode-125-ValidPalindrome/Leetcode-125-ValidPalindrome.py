class Solution(object):
    def isPalindrome(self, s):
        filtered = []
        for char in s:
            if char.isalnum():
                filtered.append(char.lower())

        length = len(filtered)

        for i in range(length//2):
            if filtered[i] != filtered[length-i-1]:
                return False
            
        return True

# class Solution(object):
#     def isPalindrome(self, s):
#         s = s.lower()
#         s = re.sub('[^a-z0-9]', '', s)

#         return s == s[::-1]