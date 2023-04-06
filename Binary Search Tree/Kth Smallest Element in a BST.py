# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        outArr = []
        def inOrder(node):
            if not node or len(outArr) == k:
                return
            
            inOrder(node.left)
            outArr.append(node.val)
            inOrder(node.right)

        inOrder(root)
        print(outArr)
        return outArr[k-1]
        #if k-1 >= 0 and outArr:
        #    return outArr[k-1]