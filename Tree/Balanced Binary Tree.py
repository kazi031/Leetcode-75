# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        
        Flag = []

        def heightCheck(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            else:
                leftHeight = 1 + heightCheck(root.left)
                rightHeight = 1 + heightCheck(root.right)
                if abs(rightHeight - leftHeight) > 1:
                    Flag.append(False)
                return max(leftHeight, rightHeight)
        
        heightCheck(root)
        
        if Flag:
            return False
        else:
            return True