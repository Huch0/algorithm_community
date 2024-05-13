# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 
# 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 
# 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

# 4 0
# -7 -3 5 8

# 3 3
# 3 3 3

# 6 0
# 0 0 0 0 0 0

# 7 0
# -7 -3 -2 5 8 0 0

N, S = map(int, input().split())

line = input().split()
zero_count = 0

nums = []

for n in line:
    n = int(n)
    if n == 0:
        zero_count += 1
        continue
    nums.append(n)

N = N - zero_count

is_used = [False] * N

count = 0

def fun(cur, tot):
    global count
    if cur == N:
        if tot == S:
            count += 1
        return
    
    fun(cur+1, tot)
    fun(cur+1, tot + nums[cur])

fun(0, 0)
if S == 0:
    print(count * 2 ** zero_count - 1)
else:
    print(count * 2 ** zero_count)