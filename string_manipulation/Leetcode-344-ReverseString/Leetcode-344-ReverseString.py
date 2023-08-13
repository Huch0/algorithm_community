class Solution(object):
    def reverseString(self, s):
        length = len(s)
        for i in range(length//2):
            s[i], s[length-i-1] = s[length-i-1], s[i]


# class Solution(object):
#     def reverseString(self, s):
#         s.reverse()