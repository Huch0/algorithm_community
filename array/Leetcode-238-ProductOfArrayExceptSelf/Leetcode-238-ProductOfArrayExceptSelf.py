class Solution(object):
    def productExceptSelf(self, nums):
        output = []
        product = 1
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                counter += 1
        for i in range(len(nums)):
            if counter >= 2:
                output.append(0)
            elif counter == 1:
                if nums[i] != 0:
                    output.append(0)
                else:
                    output.append(product)
            else:
                output.append(product / nums[i])

        return output

# class Solution(object):
#     def productExceptSelf(self, nums):
#         out = []
#         p = 1
#         for i in range(len(nums)):
#             out.append(p)
#             p *= nums[i]
#         p = 1
#         for i in range(len(nums) - 1, -1, -1):
#             out[i] *= p
#             p *= nums[i]
#         return out