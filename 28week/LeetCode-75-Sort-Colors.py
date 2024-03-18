class Solution:

    # [2,0,2,1,1,0]
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def is_heap(index):
            if index == 0:
                return True
            if nums[index] <= nums[(index+1) // 2 - 1]:
                return True
            return False

        def down_heap(index):
            nums[index], nums[(index+1) // 2 - 1] = nums[(index+1) // 2 - 1], nums[index]
            if not is_heap((index+1) // 2 - 1):
                down_heap((index+1) // 2 - 1)

        def heap_pop(index):
            if index == len(nums)-1:
                return
            nums[0], nums[-(index+1)] = nums[-(index+1)], nums[0]
            up_heap(len(nums) - index)

        def up_heap(final_index):
            i = 1
            while i*2 < final_index:
                if i*2+1 < final_index:
                    if nums[i - 1] < nums[i*2 - 1] or nums[i - 1] < nums[i*2]:
                        if nums[i*2 - 1] < nums[i*2]:
                            nums[i - 1], nums[i*2] = nums[i*2], nums[i - 1]
                            i = i*2 + 1
                        else:
                            nums[i - 1], nums[i*2-1] = nums[i*2-1], nums[i - 1]
                            i = i*2
                    else:
                        break
                else:
                    if nums[i - 1] < nums[i*2 - 1]:
                        nums[i - 1], nums[i*2 - 1] = nums[i*2 - 1], nums[i - 1]
                        i = i*2
                    else:
                        break
        # heap push
        # [2,0,2,1,1,0] -> [2,1,2,0,1,0]
        for i in range(len(nums)):
            if not is_heap(i):
                down_heap(i)

        # nums.reverse()
        #print(nums)

        # heap 
        # [2,1,2,0,1,0] -> [0,0,1,1,2,2]
        for i in range(len(nums)):
            heap_pop(i)

        print(nums)