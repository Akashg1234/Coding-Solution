# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        list_length=1
        temp=head
        
        while temp.next:
            temp=temp.next
            list_length+=1
            
        temp.next=head
        
        lastElement = head
        
        k=k%list_length
        
        
        for _ in range(list_length-k-1):
            lastElement = lastElement.next
            
        new_head = lastElement.next
        lastElement.next  = None
        
        return new_head
