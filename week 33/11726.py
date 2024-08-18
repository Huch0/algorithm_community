import sys, math

N = int(sys.stdin.readline())
count=0
a=N//2

for i in range(a+1):
    tile_counts = {'block': i, '2': N-2*i }
     # Step 2: Calculate the total number of fruits
    n = sum(tile_counts.values())  # Total number of fruits

    # Step 3: Calculate the denominator product of factorials of the counts
    denominator = math.prod(math.factorial(count) for count in tile_counts.values())

    # Step 4: Calculate the number of distinct permutations
    count += math.factorial(n) // denominator    

print(count)