def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    
    return sum
