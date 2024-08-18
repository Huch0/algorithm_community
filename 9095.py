import math
from collections import Counter

n=int(input())


for _ in range(n):
    num=int(input())
    count=0
    divide_3=num//3
    #remainder_3=num%3
    for i in range(divide_3,-1,-1):
        divide_2=(num-i*3)//2
        #remainder_2=(num-i*3)%2
        for j in range(divide_2,-1,-1):
            # Step 1: Define the fruit counts directly
            fruit_counts = {'3': i, '2': j, '1':num-i*3-j*2 }

            # Step 2: Calculate the total number of fruits
            n = sum(fruit_counts.values())  # Total number of fruits

            # Step 3: Calculate the denominator product of factorials of the counts
            denominator = math.prod(math.factorial(count) for count in fruit_counts.values())

            # Step 4: Calculate the number of distinct permutations
            count += math.factorial(n) // denominator    
    print(count)        
