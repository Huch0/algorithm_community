N,r,c = map(int,input().split())

start = 0
end = 2**(N*2)-1


while N > 1:
    
    temp = end - start + 1
    
    if r >= 2**(N-1):
        if c >= 2**(N-1): # Z 순서상 4번째(마지막)
            start += temp//4*3
            N -= 1
            r -= 2**N
            c -= 2**N
        else: # Z 순서상 3번째
            start += temp//4*2
            end -= temp//4
            N -= 1
            r -= 2**N
    else: 
        if c >= 2**(N-1): # Z 순서상 2번째
            start += temp // 4
            end -= temp // 2
            N -= 1
            c -= 2**N
        else: # Z 순서상 1번째
            end -= temp // 4 * 3
            N -= 1

if r == 0 and c == 0:
    print(start)
elif r == 0 and c == 1:
    print(start + 1)
elif r == 1 and c == 0:
    print(end - 1)
else:
    print(end)