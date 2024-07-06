class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = len(s)
        result = ""

        for i in range(len(s)) :
            if s[i] in t : 
                count = 0
                list_of_t = list(t)
                for j in range(i,len(s)) :
                    
                    if s[j] in list_of_t : 
                        list_of_t.remove(s[j])
                        count += 1
                    
                    if count == len(t) :
                        if j-i+1 < min_len : result = s[i:j+1]
            
        return result