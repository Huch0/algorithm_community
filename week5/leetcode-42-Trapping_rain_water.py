#투포인터
class Solution:
    def trap(self, height: List[int]) -> int:
        waterSum = 0
        lindex, rindex = 0, len(height)-1
        lmax, rmax = height[lindex], height[rindex]
        while lindex != rindex:
            if lmax >= rmax:
                rindex -= 1
                rmax = max(rmax, height[rindex])
                waterSum += (rmax - height[rindex])
            else:
                lindex += 1
                lmax = max(lmax, height[lindex])
                waterSum += (lmax - height[lindex])
        return waterSum

#처음 pass한 풀이 . 칸을 하나하나 확인하니 시간초과 걸려서 (수면높이 - 바닥)으로 계산하도록 짰음
class Solution:
    def trap(self, height: List[int]) -> int:
        waterSum = 0
        for i in range(max(height), 0, -1):
            left_standard = 0
            right_standard = 0
            for j in range(len(height)):
                if height[j] >= i:
                    left_standard = j
                    break
            for j in range(len(height)-1, -1, -1):
                if height[j] >= i:
                    right_standard = j
                    break
            if left_standard != right_standard:
                for j in range(left_standard+1, right_standard):
                    if height[j] < i:
                        waterSum += (i - height[j])
                del height[left_standard+1:right_standard]
            if len(height) == 0:
                break
        return waterSum

# 브루트포스 해봤는데 시간제한 걸림
def trap(self, height: List[int]) -> int:
    waterSum = 0
    maxheight = max(height)
    for h in range(1, maxheight+1):
        for index, ground in enumerate(height):
            if ground >= h:
                left_standard = index
                break
        reversed_height = height[:]
        reversed_height.reverse()
        for index, ground in enumerate(reversed_height):
            if ground >= h:
                right_standard = len(height) - 1 - index
                break
        if left_standard != right_standard:
            for i in height[left_standard : right_standard + 1]:
                if i < h:
                    waterSum += 1
    return waterSum

# 좀 많이 줄인 브루트포스인데 .. 시간제한 걸림. 이런 방법으론 안되는듯 ? ; 
def trap(self, height: List[int]) -> int:
    waterSum = 0
    for i in range(1, len(height)):
        if height[i-1] > height[i]:
            for j in range(height[i]+1, height[i-1]+1):
                for k in range(i+1, len(height)):
                    if height[k] >= j: 
                        waterSum += (k-i)
                        break;    
    return waterSum
