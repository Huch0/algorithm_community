class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def a_is_bigger_than_b(a,b) :
            char_a = str(a)
            char_b = str(b)

            if char_a[0] > char_b[0] : return True
            elif char_a[0] == char_b[0] : 
                x = int(char_a + char_b)
                y = int(char_b + char_a)
                if x > y : return True
                else : return False 
            else : return False
        
        key = 1

        while(key < len(nums)) :
            cur = key-1
            temp = nums[key]
            
            while(cur>0) :
                if a_is_bigger_than_b(nums[cur],temp) :
                    nums[cur+1] = temp
                    break
                else : 
                    nums[cur+1] = nums[cur]
                    cur -= 1

            if cur == 0 :
                if a_is_bigger_than_b(temp, nums[cur]):
                    nums[cur+1] = nums[cur]
                    nums[cur] = temp
                else :
                    nums[cur+1] = temp
            key += 1
        
        return str(int(''.join(map(str,nums))))
                
        