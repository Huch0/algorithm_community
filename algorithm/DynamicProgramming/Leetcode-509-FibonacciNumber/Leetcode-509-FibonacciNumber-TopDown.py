import collections

dic = collections.defaultdict()

def fib(N:int) -> int :
    if N <= 1 : return N
    
    if N not in dic : 
        dic[N] = fib(N-1) + fib(N-2)
    
    return dic[N]    
