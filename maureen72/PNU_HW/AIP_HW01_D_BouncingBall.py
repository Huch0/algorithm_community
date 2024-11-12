coefficient = float(input("Enter coefficient of restitution: "))
initialHeight = float(input("Enter initial height in meters: "))

# initialize cnt as 1 -> 최소 한번은 튀기 때문에
cnt = 1

# 공이 처음 떨어질 때의 거리만큼 이동하므로, 총 이동 거리를 초기 높이로 초기화
distance = initialHeight

# 첫 번째 바운스의 높이를 coefficient를 이용해 계산
height = initialHeight * coefficient

# 공이 튕긴 후 높이가 0.1미터(10cm) 이상일 때까지 반복
while height >= 0.1:
    # 공이 내려갔다가 올라오는 거리(두 배의 높이)를 총 이동 거리로 더함
    distance += height * 2
    
    # cnt 증가
    cnt += 1
    
    # 다음 바운스 높이를 반발 계수를 이용해 계산
    height *= coefficient    

print(f"Number of bounces: {cnt}")
print(f"Meters traveled: {distance:.2f}")
