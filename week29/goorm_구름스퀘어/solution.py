n = int(input())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))

schedule.sort(key=lambda x: (x[1])) #끝나는 시간이 중요, 가장 빨리 끝나는 것들을 

answer = 0
cur_end_time = 0

for start, end in schedule:
    if start > cur_end_time:
        cur_end_time = end
        answer += 1

print(answer)
