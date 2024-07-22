def findContentChildren(g : list[int], s : list[int]) -> int:
    g.sort()
    s.sort()
    
    count = 0
    child_pointer = 0
    cookie_pointer = 0
    while child_pointer < len(g) and cookie_pointer < len(s) :
        if g[child_pointer] <= s[cookie_pointer] : 
            count += 1
            child_pointer += 1
        cookie_pointer += 1

    return count 

print(findContentChildren([1,2,3],[1,1]))
    