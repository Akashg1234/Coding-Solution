# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import choice

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nodeval=[]
        self.insertVal(head)
        
    def insertVal(self,head):
        temp=head
        while temp:
            self.nodeval.append(temp.val)
            temp=temp.next
            
    def getRandom(self) -> int:
        return choice(self.nodeval)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
