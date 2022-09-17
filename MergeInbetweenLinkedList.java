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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        
        ListNode list2temp = list2,
        curr=list1.next,
        pre=list1;
        
        int count=1;
        
        while(list2temp.next!=null){
            list2temp = list2temp.next;
        }
        
        while(count!=a){
            count++;
            curr=curr.next;
            pre=pre.next;
        }
        
        pre.next=list2;
        
        while(count!=b){
            count++;
            curr=curr.next;
        }
        
        list2temp.next = curr.next;
        
        return list1;
    }
}
