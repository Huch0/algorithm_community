#투포인터
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            lindex, rindex = i+1, len(nums)-1
            while lindex < rindex:
                sum = nums[i] + nums[lindex] + nums[rindex]
                if sum > 0:
                    rindex -= 1
                    continue
                if sum < 0:
                    lindex += 1
                    continue
                
                answer.append([nums[i], nums[lindex], nums[rindex]])
                while lindex < rindex and nums[lindex] == nums[lindex + 1]:
                    lindex += 1
                while lindex < rindex and nums[rindex] == nums[rindex - 1]:
                    rindex -= 1
                lindex += 1
                rindex -= 1
        return answer

#bfs 비슷한 ... 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        poslist, neglist = [], []
        for n in nums:
            if n>=0:
                poslist.append(n)
            else:
                neglist.append(n)

        poslist.sort()
        neglist.sort()
        
        for i in range(len(poslist)-1):
            for j in range(i+1 ,len(poslist)):
                if -(poslist[i] + poslist[j]) in neglist:
                    if [poslist[i], poslist[j], -(poslist[i]+poslist[j])] not in answer:
                        answer.append([poslist[i], poslist[j], -(poslist[i]+poslist[j])])

        for i in range(len(neglist)-1):
            for j in range(i+1 ,len(neglist)):
                if -(neglist[i] + neglist[j]) in poslist:
                    if [neglist[i], neglist[j], -(neglist[i]+neglist[j])] not in answer:
                        answer.append([neglist[i], neglist[j], -(neglist[i]+neglist[j])])

        if poslist.count(0) >= 3:
            answer.append([0,0,0])

        return answer