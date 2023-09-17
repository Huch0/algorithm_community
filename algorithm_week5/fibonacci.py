def fibo(x): 
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(5))

d = [0] * 100 # 큰 문제에서 다시 쓸 값들을 저장할 메모리 확보

def TopDownFibo(x): # 탑다운 방식
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0: # 값이 저장된 적이 있으면 그걸 그대로 쓰면 된다. 일반적인 피보나치에서는 다시 연산을 해야 함
        return d[x]
    
    d[x] = TopDownFibo(x-1) + TopDownFibo(x-2) # 값이 저장된 된 적이 없으면 초기화해주기. 이건 다음에 가져다쓴다.
    return d[x]

print(TopDownFibo(99))

def BottomUpFibo(x):
    d = [0] * 100 # 마찬가지로 재사용 가능한 배열 초기화
    d[1] = 1
    d[2] = 1
    n = x
    
    for i in range(3, n+1): # 반복문을 이용해서 차근차근 d[99]까지 도달하는 방식.
        d[i] = d[i-1] + d[i-2]
        
    return d[n]

print(BottomUpFibo(99))