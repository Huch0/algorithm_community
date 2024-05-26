"""
Task :
A(n) = (n/2 if k is even, else (n+1)), n : integer
there is a function f(n) : n,A(n),A(A(n)), ... which repeat A(n) until it gets the value 1
For example, if we start at 9

    9 -> 10 -> 5 -> 6 -> 3 -> 4 -> 2 -> 1
    
g(n) -> the number of steps for 1 from starting n. for example) g(9) = 7
h(n) -> the number of integers which saticfy g(m) = n. for example) h(7) = 13

write a program to compute h(n)

Input :
The first input line is the starting integer n (1 <= m <= 40000)

Output :
Print only one integer m result of h(n) (modulo 1000007) 
"""

import math

n = int(input())
result = 0

for index,i in enumerate(range(n-1,n//2-1,-1)) :
    result += math.comb(i,index)
    
print(result%1000007)
