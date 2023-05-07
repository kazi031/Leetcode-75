class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        else:
            target = sum(nums) // 2
        
        dp = set()
        dp.add(0)
        
        for i in range(len(nums) - 1, -1, -1):
            # Can't Update dp while iterating through
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            
            dp = nextDP
        
        if target in dp:
            return True
        else:
            return False