# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insertIntoBST(nums, left, right) -> Optional[TreeNode]:
            if left > right:
                return None
            middle = (left + right) // 2
            newNode = TreeNode(nums[middle], None, None)
            newNode.left = insertIntoBST(nums, left, middle - 1)
            newNode.right = insertIntoBST(nums, middle + 1, right)
            return newNode
        
        return insertIntoBST(nums, 0, len(nums)-1)