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
    private ListNode reverseList(ListNode start){
        ListNode pre=null,temp=start;
        while(temp!=null){
            ListNode temp2 = temp.next;
            temp.next=pre;
            pre=temp;
            temp=temp2;
        }
        return pre;
    }
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head==null || head.next==null){return head;}

        int count=1;
        ListNode dummy= new ListNode(0),end=null,temp=head,start=null,pre=null;
        dummy.next=head;
        pre=dummy;

        while(count<left){
            // System.out.println("till left->"+temp.val);
            
            count++;
            pre=pre.next;
            temp=temp.next;
        }

        start = temp;
// System.out.println("start->"+start.val+"Pre:"+pre.val);
        while(count<=right-1){
            System.out.println("till right->"+temp.val);
            count++;
            temp=temp.next;
        }

        end=temp.next;
        temp.next=null;
        // System.out.println("end->"+temp.val);
        pre.next = reverseList(start);
        start.next = end;

        return dummy.next;

    }
}
