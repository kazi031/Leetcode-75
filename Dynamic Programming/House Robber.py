2 1 1 7 3 2 
6
10
11
3rd and 4th

Code: 

class Solution:
    def rob(self, nums: List[int]) -> int:
        new_list = [0] * len(nums)
        print(new_list)

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        for i in range(len(nums)-2-1, -1, -1):
            if i + 3 == len(nums):
                new_list[i] = nums[i] + nums[i+2]
            else:
                new_list[i] = max(nums[i] + nums[i+2], nums[i] + nums[i+3])
            nums[i] = new_list[i]
        
        print(nums)
        return max(nums[0], nums[1])