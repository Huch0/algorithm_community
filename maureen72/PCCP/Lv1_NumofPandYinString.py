def solution(s):
    
    s = s.lower()
    pNum = s.count('p')
    yNUm = s.count('y')
    
    if pNum == yNUm:
        if pNum == 0:
            return True
        return True
    else:
        return False
    
    return pNum