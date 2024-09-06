import sys

computers = int(sys.stdin.readline())

contaminated = [0] * computers
contaminated[0] = 1  # Computer 1 is initially contaminated

N = int(sys.stdin.readline())

adj_list = [[] for _ in range(computers)]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a - 1].append(b - 1)  # Adjusting to 0-based index
    adj_list[b - 1].append(a - 1)  # Assuming undirected graph

def contaminate(root):
    count = 0
    stack = [root]

    while stack:
        node = stack.pop()
        for neighbor in adj_list[node]:
            if contaminated[neighbor] == 0:
                contaminated[neighbor] = 1
                count += 1
                stack.append(neighbor)

    return count

# Start the contamination from computer 1 (index 0)
count = contaminate(0)

print(count)
