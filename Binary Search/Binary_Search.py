class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1
        while l<=r:
            middle = (l+r)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return -1