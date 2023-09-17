backpack = []
n, k = map(int, input().split())
for i in range(n):
    weight, value = map(int, input().split())
    backpack.append((weight, value))
    
d = [0] * (k+1) # 이 배열은 "가치"의 배열이다. 결국 이 배열의 최댓값을 구하는 식으로 Bottom-Up 다이나믹 프로그래밍을 진행하였다.
for item in backpack:
    weight, value = item
    for i in range(k, weight-1, -1):
        d[i] = max(d[i], d[i-weight] + value) # 점화식은 d[i] = max(d[i], d[i-w] + v). 즉, 현재 상태와 어떤 물건(w,v)를 담았을 때 d[i] 중 최댓값이다.
print(d[-1])
