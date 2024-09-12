# 8 30 4 30
# 7
# 9
# 7
# 30
# 2
# 7
# 9
# 25
# -> 5

# 8 50 4 7
# 2
# 7
# 9
# 25
# 7
# 9
# 7
# 30
# -> 4

# 1. 초밥은 리스트로 입력받자
# 2. 초밥을 투 포인터로 순회하면서 중복이 없는 최대 길이를 구하자
# 3. 2번에서 만약 k길이의 초밥을 찾았다면 그 때 쿠폰에 있는 번호를 포함한건가를 따져보자
# 4. 만약 포함되지 않는다면 k길이의 초밥을 찾은 것이므로 최대 길이를 +1해서 저장하자
# 5. 만약 포함된다면 k길이의 초밥을 찾은 것이 아니므로 최대 길이를 그대로 저장하자

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
sushi.extend(sushi[:k-1])

st = 0
en = k-1
answer = 0

def cal_answer(st, en):
    set_sushi = set(sushi[st:en+1])
    if c in set_sushi:
        return len(set_sushi)
    else: 
        return len(set_sushi)+1

while en < len(sushi):
    answer = max(answer, cal_answer(st, en))
    st += 1
    en += 1
    
print(answer)