# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        if not head.next:
            return head
        
        prev = head
        curr=prev.next
        
        while curr:
            
            if prev.val != curr.val:
                prev=curr
                curr=curr.next
                
            else:
                curr=curr.next
                prev.next=curr
                
        return head
