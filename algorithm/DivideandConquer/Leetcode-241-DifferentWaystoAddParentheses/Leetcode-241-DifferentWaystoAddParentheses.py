class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left,right,op) :
            result = []
            for i in left:
                for j in right:
                    result.append(eval(str(i)+op+str(j)))
            return result 

        if expression.isdigit() : return [int(expression)]

        results = []
        for index, value in enumerate(expression) :
            if value in "+-*" :
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                results.extend(compute(left,right,value))

        return results