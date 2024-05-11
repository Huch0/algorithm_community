# 자연수 N과 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 4 2

# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3

N, M = map(int, input().split())

# back tracking

sequence = []
is_used = [False] * N

def fun(n):
    if n == M:
        for i in sequence:
            print(i, end = " ")
        
        print()
        return
    
    for i in range(N):
        if not is_used[i]:
            sequence.append(i+1)
            is_used[i] = True
            fun(n+1)
            sequence.pop()
            is_used[i] = False
    
fun(0)
        