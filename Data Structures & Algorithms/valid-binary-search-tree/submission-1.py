# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr : 
                return []
            
            return dfs(curr.left) + [curr.val] + dfs(curr.right)
        
        arr = dfs(root)

        if not arr or len(arr) == 1:
            return True

        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        
        return True