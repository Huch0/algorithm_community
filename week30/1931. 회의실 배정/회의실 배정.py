import sys
input = sys.stdin.readline

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
dst = 0 
for s,d in meetings:
    if s >= dst:
        dst = d
        cnt+=1

print(cnt)
 
        