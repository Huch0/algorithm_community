def str_to_list_with_alpha_num(s: str) -> list:
    result = []

    for char in s:
        #Upper char change to Lower char and append
        if('A' <= char <= 'Z'):
            char = chr(ord(char) - ord('A') + ord('a'))

        elif('a' <= char <= 'z'):
            pass

        elif('0' <= char <= '9'):
            pass

        #if char is not alpha, no append
        else:
            continue

        result.append(char)

    return result

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_to_list = str_to_list_with_alpha_num(s)
        if s_to_list == list(reversed(s_to_list)):  
            return True
        else:
            return False