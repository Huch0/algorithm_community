# Knapsack Problem

The knapsack problem is a classic optimization problem in computer science and mathematics. It involves selecting items to maximize the total value while staying within the weight capacity of a knapsack.

There are three main types of knapsack problems:

1. **0/1 Knapsack Problem**: In this variation, each item can be selected at most once. The goal is to maximize the total value of the selected items without exceeding the weight capacity of the knapsack.

2. **Unbounded Knapsack Problem**: In this variation, each item can be selected an unlimited number of times. The goal is to maximize the total value of the selected items without exceeding the weight capacity of the knapsack.

3. **Fractional Knapsack Problem**: In this variation, items can be selected in fractions. The goal is to maximize the total value of the selected items without exceeding the weight capacity of the knapsack.

The 0/1 knapsack problem is the most commonly studied variation and is known for its importance in the field of dynamic programming.

## 0/1 Knapsack Problem

### Problem Statement

Given a set of items, each with a weight and a value, determine the number of each item to include in a knapsack so that the total weight is less than or equal to a given limit and the total value is maximized.

### Example

Suppose we have the following items:

| Item | Weight | Value |
|------|--------|-------|
| A    | 2      | 6     |
| B    | 2      | 10    |
| C    | 3      | 12    |
| D    | 4      | 13    |

And a knapsack with a weight capacity of 7.

The optimal solution is to select items B and C, which have a total weight of 5 and a total value of 22.

### Approach

- Subproblem: For each item, we have two choices: include it in the knapsack or exclude it.
- State: The state of the problem can be defined by the item index and the remaining capacity of the knapsack.
- Base Case: If the item index is less than 0 or the capacity is 0, the value is 0.
- Transition: If the weight of the current item is greater than the remaining capacity, we exclude the item. Otherwise, we consider both including and excluding the item and choose the option that maximizes the total value.

Here is an example of a recursive solution to the 0/1 knapsack problem using memoization:

```python
def knapsack(items, capacity, index, memo={}):
    if (index, capacity) in memo:
        return memo[(index, capacity)]
    if index < 0 or capacity == 0:
        return 0
    if items[index][0] > capacity:
        result = knapsack(items, capacity, index - 1, memo)
    else:
        include = items[index][1] + knapsack(items, capacity - items[index][0], index - 1, memo)
        exclude = knapsack(items, capacity, index - 1, memo)
        result = max(include, exclude)
    memo[(index, capacity)] = result
    return result

items = [("A", 2, 6), ("B", 2, 10), ("C", 3, 12), ("D", 4, 13)]
capacity = 7
print(knapsack(items, capacity, len(items) - 1)) # Output: 22
```

using tabulation:

```python
def knapsack(items, capacity):
    n = len(items)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight, value = items[i - 1][0], items[i - 1][1]
            if weight > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(value + table[i - 1][w - weight], table[i - 1][w])
    return table[n][capacity]

items = [(2, 6), (2, 10), (3, 12), (4, 13)]
capacity = 7
print(knapsack(items, capacity)) # Output: 22
```

### Complexity

Time and Space Complexity : O(n * W)

- n: number of items
- W: capacity of the knapsack
