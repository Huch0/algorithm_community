import sys
input = sys.stdin.readline

length = int(input())
nums = [0] + list(map(int,input().split()))

dp = [[0] * (length + 1) for _ in range(length + 1)] 


for _ in range(int(input())):
    S, E = map(int,input().split())
    s, e = S, E
    is_palindrome = 1
    
    while s <= e:
        if dp[s][e] == -1 or nums[s] != nums[e]:
            is_palindrome = -1
            break
        elif dp[s][e]:
            break
        s, e = s + 1, e - 1
    
    for i in range(S, s):
            dp[i][S+E-i] = is_palindrome
    print(1 if is_palindrome == 1 else 0)
