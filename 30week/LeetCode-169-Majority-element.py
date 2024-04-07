from collections import Counter, defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Counter를 이용한 풀이 180ms
        # counter = Counter(nums)
        # max_element = max(counter, key=counter.get)

        # if counter[max_element] > len(nums) // 2:
        #     return max_element

        #Sorting을 이용한 풀이, 절반을 넘었다면 중앙값이 majority element이다. 166ms
        #return sorted(nums)[len(nums) // 2]

        #단순 dictionary를 이용한 풀이 ,188ms
        # voting = defaultdict(int)

        # for num in nums:
        #     voting[num] += 1
        #     if voting[num] > len(nums) // 2:
        #         return num

        # dictionary에 dp를 이용, 168 ms
        # voting = defaultdict(int)
        # for num in nums:
        #     if voting[num] == 0:
        #         voting[num] = nums.count(num)
            
        #     if voting[num] > len(nums) // 2:
        #         return num
        
        # 분할 정복을 이용한 풀이, 219 ms
        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2

        left = self.majorityElement(nums[:mid])
        right = self.majorityElement(nums[mid:])

        return [left, right][nums.count(right) > mid]