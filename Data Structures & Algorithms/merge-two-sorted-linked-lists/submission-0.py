# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i, j = list1, list2
        dummy = node = ListNode()
        

        while j and i:
            if j.val < i.val:
                node.next = j
                j = j.next
            else:
                node.next = i
                i = i.next
            node = node.next

        node.next = i or j


        return dummy.next