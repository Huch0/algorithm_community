

import sys

N, M = map(int,sys.stdin.readline().split())

passwords={}
for _ in range(N):
    name, password = sys.stdin.readline().split()
    passwords[name]=password

for _ in range(M):
    search=sys.stdin.readline().rstrip()
    print(passwords[search])
    
 