import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sequence = []

def backtrack():
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, n + 1):
        sequence.append(i)
        backtrack()
        sequence.pop()

backtrack()