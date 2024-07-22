import bisect

def findContentChildren(g : list[int], s : list[int]) -> int:
    g.sort()
    s.sort()
    
    result = 0
    for i in s :
        index = bisect.bisect_right(g,i) 
        if index > result : result += 1
    return result
    

print(findContentChildren([1,2],[1,2,3]))
    