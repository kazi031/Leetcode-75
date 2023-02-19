# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        result = [[root.val]]
        current_level = [root]
        while current_level:
            next_level, row_val = [], []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                    row_val.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    row_val.append(node.right.val)
            if row_val:
                result.append(row_val)
            current_level = next_level.copy()
        return result