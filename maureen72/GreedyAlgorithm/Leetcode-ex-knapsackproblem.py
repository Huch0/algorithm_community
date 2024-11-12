def frational_knapsack(cargo):
    capacity = 15
    pack = []
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)
    
    total_value = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            #fraction = capacity / p[2]
            total_value += p[0] * capacity
            break
    return total_value