# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        dl, dr = self.maxDepth(root.left), self.maxDepth(root.right)

        if dl > dr:
            return dl + 1
        else: 
            return dr + 1 


        