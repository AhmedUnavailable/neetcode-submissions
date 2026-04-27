# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev =  None
        i = head

        while i:
            next = i.next
            i.next = prev

            prev = i
            i = next
            

        return prev

            
                     