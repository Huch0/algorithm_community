class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        # Sort the list to use two pointer
        nums.sort()

        # Pick ith_nums
        for i in range(len(nums) - 2):
            # if there is duplicate, skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                triplet = [nums[i], nums[left], nums[right]]
                triplet_sum = sum(triplet)

                if triplet_sum > 0:
                    right -= 1
                elif triplet_sum < 0:
                    left += 1
                else:
                    triplets.append(triplet)

                    # move pointers until there is no duplicate
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return triplets
