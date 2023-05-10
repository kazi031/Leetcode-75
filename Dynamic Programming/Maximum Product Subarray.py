class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
                continue
            tmp = n * curMax
            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, curMin * n, tmp)
            res = max(res,curMax)
        
        return res