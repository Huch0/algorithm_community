def majorityElement(nums: list[int]) -> int: 
    nums.sort()
    check = nums[0]
    count = 1
    for i in range(1,len(nums)) :
        if check == nums[i] :
            count += 1
        else : 
            check = nums[i]
            count = 1
        
        if count > len(nums)//2 : 
            return nums[i]

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))