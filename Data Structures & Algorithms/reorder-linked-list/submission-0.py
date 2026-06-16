# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = self.len(head)
        m = n // 2
        i = 1
        curr = head
        while curr and i <= m:
            curr = curr.next
            i += 1

        
        list1 = head
        list2 = self.reverse(curr.next)
        curr.next = None

        while  list2:
            t1 = list1.next
            t2 = list2.next

            list1.next = list2
            list2.next = t1
            
            list1, list2 = t1, t2

        

    def len(self, head):
        n = 0
        while head:
            n += 1
            head = head.next
        return n
    
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        