class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        negetives = [num for num in nums if num < 0]
        positives = [num for num in nums if num > 0]

        if nums.count(0) > 0:
            for negetive in negetives:
                if negetive*(-1) in positives and [negetive, 0, negetive*(-1)] not in result:
                    result.append([negetive, 0, negetive*(-1)])

            if nums.count(0) >= 3:
                result.append([0, 0, 0])

        for i in range(len(positives)):
            for j in range(len(negetives)):
                
                if positives[i] + negetives[j] == 0:
                    continue
                if (-1)*(positives[i] + negetives[j]) in positives:
                    elem = [negetives[j], positives[i], (-1)*(positives[i] + negetives[j])]                    
                elif (-1)*(positives[i] + negetives[j]) in negetives:
                    elem = [(-1)*(positives[i] + negetives[j]), negetives[j], positives[i]]
                else:
                    continue
                elem.sort()
                if elem[0] == elem[1] or elem[1] == elem[2]:
                    if positives.count(elem[1]) == 1 or negetives.count(elem[1]) == 1:
                        continue

                if elem not in result:
                    result.append(elem)

        return result
        
