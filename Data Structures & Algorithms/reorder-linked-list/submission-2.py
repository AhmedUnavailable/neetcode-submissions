# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next

        
        list1 = head
        list2 = self.reverse(s.next)
        s.next = None

        while  list2:
            t1 = list1.next
            t2 = list2.next

            list1.next = list2
            list2.next = t1
            
            list1, list2 = t1, t2

    
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        