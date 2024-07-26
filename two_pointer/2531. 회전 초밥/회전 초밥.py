import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

# 초밥의 종류를 카운트할 리스트와 현재 윈도우에서의 초밥 수를 저장할 변수들 초기화
sushi_count = [0] * (d + 1)
current_sushi = 0

# 초기 윈도우 설정
for i in range(k):
    if sushi_count[sushi[i]] == 0:
        current_sushi += 1
    sushi_count[sushi[i]] += 1

# 쿠폰 초밥 추가
max_sushi = current_sushi
if sushi_count[c] == 0:
    max_sushi += 1

# 슬라이딩 윈도우 적용
for i in range(1, N):
    # 윈도우의 시작 부분을 제거
    sushi_count[sushi[i - 1]] -= 1
    if sushi_count[sushi[i - 1]] == 0:
        current_sushi -= 1

    # 윈도우의 끝 부분을 추가
    next_sushi = sushi[(i + k - 1) % N]
    if sushi_count[next_sushi] == 0:
        current_sushi += 1
    sushi_count[next_sushi] += 1

    # 쿠폰 초밥 추가 고려
    if sushi_count[c] == 0:
        max_sushi = max(max_sushi, current_sushi + 1)
    else:
        max_sushi = max(max_sushi, current_sushi)

print(max_sushi)
