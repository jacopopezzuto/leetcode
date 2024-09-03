# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head=node
        carry = 0
        while l1!=None or l2!=None or carry>0:
            node.next=ListNode(0)
            node=node.next
            node.val = carry
            if l1!=None:
                node.val += l1.val
                l1=l1.next
            if l2!=None:
                node.val+=l2.val
                l2=l2.next
            carry = int(node.val / 10)
            node.val= int(node.val%10)
        return head.next