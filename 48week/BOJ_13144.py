N = int(input())
A = list(map(int, input().split()))

st = 0
en = 0
answer = 0
seen = set()  # 중복 체크를 위한 집합

while st < N and en < N:
    if A[en] not in seen:
        # 중복이 없으면 현재 값을 추가하고 en을 한 칸 오른쪽으로 이동
        seen.add(A[en])
        en += 1
        answer += (en - st)
    else:
        # 중복이 있으면 st를 이동시키며 중복 값을 제거
        seen.remove(A[st])
        st += 1

print(answer)