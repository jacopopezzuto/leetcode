# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        headLower=ListNode(0)
        lower=headLower
        headHigher=ListNode(0)
        higher=headHigher
        curr=head
        while curr!=None:
            if curr.val<x:
                lower.next=curr
                lower=lower.next
            else:
                higher.next=curr
                higher=higher.next
            curr=curr.next 
        higher.next=None
        lower.next=headHigher.next
        return headLower.next
            
                