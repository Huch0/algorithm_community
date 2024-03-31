class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Define the operations in a dictionary
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

        # If the expression is a number, return it as a result
        if expression.isdigit():
            return [int(expression)]

        # Compute all possible results recursively and combine them
        return [operations[c](l, r)
                for i, c in enumerate(expression) if c in operations
                for l in self.diffWaysToCompute(expression[:i])
                for r in self.diffWaysToCompute(expression[i+1:])]
