# 4 2
# 9 8 7 1

N, M = map(int, input().split())

numbers = input().split()
numbers = [int(n) for n in numbers]
numbers.sort()

result = [0 for _ in range(M)]
is_used = [False for _ in range(N)]

def nm_5(path):
    if len(path) == M:
        #print(' '.join([numbers[p] for p in path]))
        result = [numbers[p] for p in path]
        for r in result:
            print(r, end= " ")
        print()
        return
    
    for i in range(N):
        if i not in path:
            nm_5(path + [i])
#nm_5([])
def nm_6(d):
    if d == M:
        for r in result:
            print(r, end = " ")
        print()
        return
    
    count = 0
    for i in range(N):
        if is_used[i]:
            count += 1

        if count >= d and not is_used[i]:
            result[d] = numbers[i]
            is_used[i] = True
            nm_6(d+1)
            is_used[i] = False
#nm_6(0)
def nm_7(d):
    if d == M:
        for r in result:
            print(r, end = " ")
        print()
        return
    for i in range(N): 
        result[d] = numbers[i]
        nm_7(d+1)
#nm_7(0)
def nm_8(d):
    if d == M:
        for r in result:
            print(r, end = " ")
        print()
        return
    
    check = 0
    if d > 0:
        check = result[d-1]
    for i in range(N):
        if check <= numbers[i]:
            result[d] = numbers[i]
            nm_8(d+1)
#nm_8(0)
results = []
def nm_9(d):
    if d == M:
        # if results and result != results[-1]:
        #     print(*result)
        #     results.append(result[::])
        # elif not results:
        #     print(*result)
        #     results.append(result[::])
        return
    
    for i in range(N):
        if not is_used[i]:
            is_used[i] = True
            result[d] = numbers[i]
            nm_9(d+1)
            is_used[i] = False
nm_9(0)
# for result in results:
#     for r in result:
#         print(r, end = " ")
#     print()