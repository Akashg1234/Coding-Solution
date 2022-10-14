# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self,l1,l2):
        
        newDummy=ListNode()
        curr=newDummy

        while l1 and l2:

            if l1.val<=l2.val:
                curr.next=l1
                l1=l1.next

            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next

        if l2:
            curr.next=l2
            l2=l2.next
        elif l1:
            curr.next=l1
            l1=l1.next

        return newDummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        temp,slow,fast=None,head,head

        while fast and fast.next:
            temp=slow
            slow=slow.next
            fast=fast.next.next

        temp.next = None

        l1=self.sortList(head)
        l2=self.sortList(slow)

        return self.mergeList(l1,l2)
