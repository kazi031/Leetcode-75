# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def sumCheck(root: Optional[TreeNode], totalSum) -> int:
            if not root:
                return 0
            leftSum = sumCheck(root.left, totalSum - root.val)
            rightSum = sumCheck(root.right, totalSum - root.val)
            total = leftSum + rightSum
            if root.val == totalSum:
                total = total + 1
            return total
                
        Count = sumCheck(root, targetSum)
        leftCount = self.pathSum(root.left, targetSum)
        rightCount = self.pathSum(root.right, targetSum)

        return Count + leftCount + rightCount