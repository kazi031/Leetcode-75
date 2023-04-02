# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        returnNode = TreeNode(0, left=None, right=None)

        def heightCheck(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            else:
                leftHeight = 1 + heightCheck(root.left)
                rightHeight = 1 + heightCheck(root.right)
                if leftHeight + rightHeight - 2 > returnNode.val:
                    returnNode.val = leftHeight + rightHeight - 2
                return max(leftHeight, rightHeight)
        
        heightCheck(root)
        return returnNode.val