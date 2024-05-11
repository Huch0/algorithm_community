# 자연수 N과 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 단 오름차순이어야함!

N, M = map(int, input().split())

# back tracking

sequence = []
max_used = 0

def fun(n):
    global max_used
    if n == M:
        for i in sequence:
            print(i, end = " ")
        
        print()
        return
    
    for i in range(1, N+1):
        if max_used < i:
            ori_max = max_used
            sequence.append(i)
            max_used = i
            fun(n+1)
            sequence.pop()
            max_used = ori_max

fun(0)
        