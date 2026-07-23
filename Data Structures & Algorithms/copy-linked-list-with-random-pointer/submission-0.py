"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)

        copyOf = {None: None}
        

        curr = head
        copy_pointer = dummy  
        while curr:
            copy = Node(curr.val)
            
            copy_pointer.next = copy
            copyOf[curr] = copy

            curr = curr.next
            copy_pointer = copy_pointer.next
        

        curr = head
        while curr:
            copyOf[curr].random = copyOf[curr.random] 
            curr = curr.next

        return dummy.next