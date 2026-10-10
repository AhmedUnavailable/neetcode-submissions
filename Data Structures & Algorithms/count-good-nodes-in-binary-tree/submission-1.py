# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(curr, mx):
            if not curr:
                return 
            
            if curr.val >= mx:
                nonlocal res

                res += 1

                dfs(curr.left, curr.val)
                dfs(curr.right, curr.val)  
            else:
                dfs(curr.left, mx)
                dfs(curr.right, mx)  
                
        dfs(root, root.val)
        return res

            
            
            