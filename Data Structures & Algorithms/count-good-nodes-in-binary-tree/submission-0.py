# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(curr, largest):
            if not curr:
                return 

            if not largest:
                largest = curr.val

            nonlocal res

            if curr.val >= largest:
                res += 1
                largest = curr.val
            
            dfs(curr.left, largest)
            dfs(curr.right, largest)
        
        dfs(root, None)
        return res
