class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        start, end = 0, 0
        life = k
        s_len = len(s)
        

        while end < s_len:
            cur_ch = s[start]
            while cur_ch == s[end] or life != 0:
                if cur_ch != s[end]:
                    life -= 1
                    print("life -1")
                if end < s_len - 1:
                    end += 1
                else:
                    break
                print(end)

            print(f'{life} {start} {end}')
            print("print max")
            cur_max = end - start + 1
            print(cur_max)
            
            max_length = max(cur_max, max_length)
            start += 1
            end += 1
            cur_ch = s[start]
            life = k
            
        return max_length
            