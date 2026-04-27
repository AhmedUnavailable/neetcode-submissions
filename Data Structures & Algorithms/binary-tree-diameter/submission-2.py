# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
                
        def dfs( curr):
            if not curr:
                return 0

            hl = dfs(curr.left)
            hr = dfs(curr.right)

            local_diam = hl + hr 
            nonlocal diam
            if diam <  local_diam:
                diam = local_diam

            return max(hl, hr) + 1
 

        dfs(root)
        return diam
        

    

        
    



        