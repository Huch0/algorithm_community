def majorityElement(nums: list[int]) -> int: 
    if not nums : return None
    if len(nums) == 1 : return nums[0]
    
    a = majorityElement(nums[:len(nums)//2])
    b = majorityElement(nums[len(nums)//2:])
    
    return [b,a][nums.count(a) > (len(nums)//2)]

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))