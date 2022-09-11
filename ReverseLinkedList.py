# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        resHead= ListNode()
        
        temp=head
        
        while temp:
            
            insertnode = ListNode(temp.val)
            temp = temp.next
            
            if not resHead.next:
                resHead.next = insertnode
                
            else:
                insertnode.next = resHead.next
                resHead.next = insertnode
                
            
            
        return resHead.next
        
