import itertools

# Define the number of ingredients
n = int(input())

# Initialize data structures to hold the nutrient information and cost
protein = []
fat = []
carbs = []
vitamins = []
cost = []

# Input the minimum amount required for each nutrient
min_protein, min_fat, min_carbs, min_vitamins= map(int, input().split())

# Input the nutrient information and cost for each ingredient
for i in range(n):
    p, f, c, v, co = map(int,input().split())
    
    protein.append(p)
    fat.append(f)
    carbs.append(c)
    vitamins.append(v)
    cost.append(co)

# Define a function to check if a combination meets the nutrient requirements
def meets_requirements(combination):
    total_protein = sum(protein[i] * combination[i] for i in range(n))
    if total_protein < min_protein:
        return 0
    total_fat = sum(fat[i] * combination[i] for i in range(n))
    if total_fat < min_fat:
        return 0
    total_carbs = sum(carbs[i] * combination[i] for i in range(n))
    if total_carbs < min_carbs:
        return 0
    total_vitamins = sum(vitamins[i] * combination[i] for i in range(n))
    if total_vitamins < min_vitamins:
        return 0
    return 1

# Define a function to calculate the total nutrition value of a combination
def total_nutrition_value(combination):
    return sum(protein[i] * combination[i] + fat[i] * combination[i] +
               carbs[i] * combination[i] + vitamins[i] * combination[i] for i in range(n))

# Generate all possible combinations of ingredient amounts (0 or 1 for each ingredient)
combinations = itertools.product([0, 1], repeat=n)

# Track the best combination and its cost and nutrition value
best_combination = None
min_cost = float('inf')
best_nutrition_value = float('-inf')

# Check each combination
for combination in combinations:
    if meets_requirements(combination):
        total_cost = sum(cost[i] * combination[i] for i in range(n))        
        if total_cost < min_cost:
            min_cost = total_cost
            best_combination = combination            
        elif total_cost == min_cost:
            nutrition_value = total_nutrition_value(combination)
            if nutrition_value > best_nutrition_value:
                min_cost = total_cost
                best_combination = combination  
                best_nutrition_value = nutrition_value
                

# Print the results
if best_combination is not None:
    used_ingredients = [i + 1 for i in range(n) if best_combination[i] == 1]
    print(" ".join(map(str, used_ingredients)))
else:
    print(0)