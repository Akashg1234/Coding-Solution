# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or  not head.next.next:
            return

        stack,size,temp=[],0,head

        while temp:
            stack.append(temp)
            size+=1
            temp=temp.next

        mid = size//2
        temp=head

        for i in range(mid):
            element=stack.pop()
            element.next=temp.next
            temp.next=element
            temp=temp.next.next

        temp.next=None
