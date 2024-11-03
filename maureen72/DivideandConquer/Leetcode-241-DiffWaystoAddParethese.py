class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    if op == '+':
                        results.append(l + r)
                    elif op == '-':
                        results.append(l - r)
                    elif op == '*':
                        results.append(l * r)
            return results

        # If expression is a single number, return it as an integer
        if expression.isdigit():
            return [int(expression)]

        results = []
        for idx, value in enumerate(expression):
            if value in "-+*":
                # Split expression into left and right parts
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:])
                
                # Compute combinations and extend results
                results.extend(compute(left, right, value))
                
        return results
