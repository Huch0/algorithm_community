class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for tmp in sorted(intervals, key=lambda x: x[0]):
            if ans and (ans[-1][1] >= tmp[0]):
                #it doesnt consider 'ans' interval contains 'tmp' intervals 
                #ans[-1][1] = tmp[1]
                ans[-1][1] = max(ans[-1][1],tmp[1])
            else:
                #If you use a comma when adding a list, 2D list will be made.
                #Same as ans.append(tmp)
                #ans += tmp,
                ans.append(tmp)
        
        return ans