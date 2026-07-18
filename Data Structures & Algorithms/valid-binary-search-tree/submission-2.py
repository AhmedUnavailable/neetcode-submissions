# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(curr, lb, ub):
            if not curr:
                return True
            if not(lb < curr.val < ub): 
                return False
            return valid(curr.left, lb, curr.val) and valid(curr.right, curr.val, ub)
        
        return valid(root, float("-inf"), float("inf"))