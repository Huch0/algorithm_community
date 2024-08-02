# 3
# -1
# 0
# 1

# -> 1

N = int(input())
sequence_minus = []
sequence = []
has_zero = False

for _ in range(N):
    num = int(input())
    if num < 0:
        sequence_minus.append(num)
    else:
        if num == 0:
            has_zero = True
        sequence.append(num)

sequence.sort(key = lambda x : -x)

# 음수는 음수끼리 묶는게 best
# 음수 남는거 있으면 0이랑 합치거나 0이 없다면 안 합쳐야함

# 양수는 양수끼리 큰 순서대로 묶는게 best

if sequence_minus:
    sequence_minus.sort()

sum = 0
# 음수끼리 묶어서 더하기 연산
i = 0
while len(sequence_minus) - i > 1:
    sum += sequence_minus[i] * sequence_minus[i+1]
    i += 2

if len(sequence_minus) - i == 1:
    #만약 0이 있으면 
    #0이랑 묶은 것으로 쳐서 노 카운트
   
    #아니면 그대로 더함
    if not has_zero:
        sum += sequence_minus[-1]

# 양수끼리 묶어서 더하기 연산
i = 0
while len(sequence) - i > 1:
    n1 = sequence[i]
    n2 = sequence[i+1]
    if n1 == 0:
        break
    elif n2 == 0:
        sum += n1
        break
    elif n1 == 1 or n2 == 1:
        sum += (n1+n2)
    else:
        sum += n1 * n2
    i += 2

if len(sequence) - i == 1:
    sum += sequence[-1]

print(sum)