#자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

#10 11 12 ->

#overflow 방지해야할듯
#

A, B, C = map(int, input().split())

def rec_mod(n):
    if n == 1:
        return A % C
    if n % 2 == 0:
        return ((rec_mod(n//2)) ** 2) % C
    else:
        return (rec_mod(n-1) * A) % C
    
print(rec_mod(B))