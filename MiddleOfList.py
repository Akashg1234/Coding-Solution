# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:return head
        if not head.next: return head
        
        list_length = 0
        temp=head
        
        while temp:
            list_length+=1
            temp=temp.next
            
        mid = list_length/2 if list_length%2==0 else math.ceil(list_length/2)
        
        temp=head
        
        while temp:
            temp=temp.next
            list_length-=1
            
            if list_length==mid:
                return temp
