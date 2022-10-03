class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:return head

        dummy= ListNode()
        len,curr,dummy.next=0,head,head

        while curr:
            len+=1
            curr=curr.next

        mid = len//2
        pre,curr,curr_len=dummy,head,0

        while curr_len<mid:
            pre=pre.next
            curr=curr.next
            curr_len+=1

        pre.next=curr.next

        return dummy.next
