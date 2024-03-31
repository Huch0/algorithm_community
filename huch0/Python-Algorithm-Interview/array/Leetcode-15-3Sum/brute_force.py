class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[k] == -(nums[i] + nums[j]):
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        triplets.add(tuple(triplet))
        
        #print(triplets)
        return triplets