# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        first = second = head
        while head.next is not None:
            if first.next and first.next.next:
                first = first.next.next
            else:
                return False
            second = second.next
            if first == second:
                return True
                
            