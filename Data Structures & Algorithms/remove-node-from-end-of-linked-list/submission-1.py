# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []

        dummy = ListNode(next=head) 
        curr = nth = head
        prev = dummy
        

        for _ in range(n):
            nth = nth.next
        
        while  nth:
            nth = nth.next
            prev = curr
            curr = curr.next
        prev.next = curr.next

        return dummy.next