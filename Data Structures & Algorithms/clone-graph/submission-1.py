"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy_head = node

        copyDict = defaultdict()

        def dfs(curr):
            
            if curr in copyDict:
                return copyDict[curr] 
            
            copy = Node(curr.val)

            copyDict[curr] = copy

            for i in curr.neighbors:
                
                copy.neighbors.append(dfs(i))
                
            return copy


        return dfs(node) if node else None