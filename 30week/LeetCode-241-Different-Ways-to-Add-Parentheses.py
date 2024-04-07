from itertools import permutations

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        nums = []
        ops = []

        num = ""
        for char in expression:
            if char.isdigit():
                num += char
            else:
                nums.append(int(num))
                ops.append(char)
                num = ""
        nums.append(int(num))

        results = []
        perm = permutations([i for i in range(len(ops))])

        def perm_to_result(perm):
            results = [None] * len(ops)
            travled = [False] * (len(ops)+1)

            for i in perm:
                op = ops[i]

                a, b = nums[i], nums[i+1]
                if travled[i]:
                    a = results[i-1]
                if travled[i+1]:
                    b = results[i+1]

                if op == "+":
                    calc = a + b
                elif op == "-":
                    calc = a - b
                elif op == "*":
                    calc = a * b

                results[i] = calc
                if travled[i]:
                    results[i-1] = calc
                travled[i] = True
                if travled[i+1]:
                    results[i+1] = calc
                travled[i+1] = True
            
            return results[perm[-1]]

        for p in perm:
            results.append(perm_to_result(p))

        return results