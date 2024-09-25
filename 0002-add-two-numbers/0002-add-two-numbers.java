/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode tail = dummyHead;
        int carry = 0;
        while(l1!=null || l2!=null || carry!=0){
            int val1 = l1!=null ? l1.val : 0;
            int val2 = l2!=null ? l2.val : 0;
            tail.next = new ListNode((val1+val2+carry)%10);
            carry = (val1+val2+carry)/10;
            tail = tail.next;
            l1=l1 == null ? null : l1.next;
            l2=l2 == null ? null : l2.next;
        }
        return dummyHead.next;
    }
}