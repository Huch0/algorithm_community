class Solution:
    operators = ['+', '-', '*']

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Conquer
        # expression only has an operand
        if len(expression) <= 2:
            return [int(expression)]

        results = []
        for i, c in enumerate(expression):
            if c in Solution.operators:
                # Divde
                # <expr> -> <expr> <op> <expr>
                lresults = self.diffWaysToCompute(expression[:i])
                rresults = self.diffWaysToCompute(expression[i + 1:])

                # Combine
                # Combine all possible results from each side
                for l in lresults:
                    for r in rresults:
                        if c == '+':
                            results.append(l + r)
                        elif c == '-':
                            results.append(l - r)
                        else:
                            results.append(l * r)
        return results
