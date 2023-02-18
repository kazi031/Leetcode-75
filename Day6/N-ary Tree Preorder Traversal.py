"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            for i in node.children:
                dfs(i)
        dfs(root)
        return result