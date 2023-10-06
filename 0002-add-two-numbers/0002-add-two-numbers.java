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
        ListNode result=new ListNode();
        ListNode l=result;
        int report =0;
        while(l1!=null || l2!=null){
            int val1=(l1!=null)?l1.val:0;
            int val2=(l2!=null)?l2.val:0;
            int newVal = (val1+val2+(report))%10;
            report = (val1+val2+report)/10; 
            ListNode newNode= new ListNode(newVal);
            l.next=newNode;
            l=l.next;
            l1=(l1!=null)?l1.next:null;
            l2=(l2!=null)?l2.next:null;
            if(l1==null && l2==null && report>0){
                ListNode reportNode= new ListNode(report);
                l.next=reportNode;
            }
        }
        return result.next;
    }
}