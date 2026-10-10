# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(curr, l, r):
            if not curr:
                return True
            if not (l < curr.val < r):
                return False
            return valid(curr.right, curr.val, r) and valid(curr.left,  l, curr.val)



        return valid(root, float("-inf"), float("inf"))

