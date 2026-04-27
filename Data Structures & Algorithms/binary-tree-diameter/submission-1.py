# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter =  0


        def dfs(head):
            nonlocal diameter
            if not head:
                return 0
            
            left = dfs(head.left)
            right = dfs(head.right)

            local_diameter = left + right

            if local_diameter > diameter:
                diameter = local_diameter

            return max(left,  right) + 1

        print(dfs(root))
        return diameter




    



        