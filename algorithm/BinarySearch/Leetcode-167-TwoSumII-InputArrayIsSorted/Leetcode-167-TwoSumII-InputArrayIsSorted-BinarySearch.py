class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1,-1,-1) :
            index = bisect.bisect_left(numbers,target-numbers[i])
            if index < len(numbers) and target-numbers[i] == numbers[index]:
                return [index+1, i+1]
            