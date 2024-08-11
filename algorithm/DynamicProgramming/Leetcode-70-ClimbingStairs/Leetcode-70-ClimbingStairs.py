import collections

count = 0
dic = collections.defaultdict(int)

def ClimbingStairs(n:int) -> int :
    if n == 1 : return 1
    if n == 2 : return 2
    if n in dic : return dic[n]
    dic[n] = ClimbingStairs(n-1)+ClimbingStairs(n-2)
    return dic[n]

print(ClimbingStairs(5))