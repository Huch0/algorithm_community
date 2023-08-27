from typing import List

class Solution:
    def fourSum(self, numbers: List[int], target: int) -> List[List[int]]:
        result = []
        numbers.sort()
        n = len(numbers)
        
        for i in range(n - 3):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    s = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                    
                    if s == target:
                        result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        
                        while left < right and numbers[left] == numbers[left + 1]:
                            left += 1
                        
                        while left < right and numbers[right] == numbers[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    
                    elif s < target:
                        left += 1
                    
                    else:
                        right -= 1
                    
        return result

