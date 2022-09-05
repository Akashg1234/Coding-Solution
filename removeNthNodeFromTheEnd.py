# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        list_length=0
        
        temp=head
        
        while temp:
            list_length+=1
            temp=temp.next
        
        if list_length==n:
            return head.next
        
        temp=head
        print(list_length)
        for i in range(1, list_length-n):
            print("i",i)
            print(temp.val)
            temp=temp.next
            
        temp.next = temp.next.next
        
        return head
        
        
