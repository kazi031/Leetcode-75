class Solution(object):
    def twoSum(self, nums, target):
        #CompMap = dict() Can be also done using dictionary
        CompMap = {}
        for i in range(len(nums)):
            n = nums[i] 
            comp = target - n
            if n in CompMap:
                return [CompMap[n], i]
            else:
                CompMap[comp] = i; 