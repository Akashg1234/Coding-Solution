# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self,head):
        if not head:return head

        prev=None
        while head:
            temp=head.next
            head.next = prev
            prev=head
            head=temp
        return prev

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        prev , newHead,dummy.next = dummy, ListNode() ,head

        len=1

        while len<10**5 and head:
            tail ,j= head,1

            while j<len and tail and tail.next:
                tail = tail.next
                j+=1

            newHead=tail.next

            if j%2==0:
                tail.next=None
                prev.next = self.reverseList(head)
                prev = head
                head.next = newHead
                head = newHead

            else:
                prev = tail
                head = newHead

            len+=1 

        return dummy.next
