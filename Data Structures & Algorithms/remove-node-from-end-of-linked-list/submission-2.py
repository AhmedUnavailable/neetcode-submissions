# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = dummy = ListNode()
        curr = dummy.next = head

        nth = curr

        for _ in range(n):
            nth = nth.next
        
        while nth:
            curr = curr.next
            nth = nth.next 
            prev = prev.next
        
        prev.next = curr.next


        return dummy.next
        