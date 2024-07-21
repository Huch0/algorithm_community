import collections

def leastlnterval(tasks: list[str], n: int) -> int:
    counter = collections.Counter(tasks)
    result = 0
    while True :
        sub = 0
        for task,_ in counter.most_common(n+1) :
            sub += 1
            result += 1
            
            counter[task] -= 1
            counter += collections.Counter()
            
        if not counter :
            break
        
        result += n - sub + 1
    
    return result
    
print(leastlnterval(['a','a','a','b','b','b'],4))
            
    
    