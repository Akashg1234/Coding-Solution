# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        if not head:return 0

        curr, component, connected = head,0,0

        while curr:
            val = curr.val
            if val in nums:
                connected+=1
                
            else:
                if connected>0:
                    component+=1
                    connected=0
                
            curr=curr.next

        if connected>0:
            component+=1

        return component
