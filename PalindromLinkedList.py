# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import ceil
import gc

class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head: return head
        if not head.next: return head
        list_length=0
        temp=head
        while temp:
            list_length+=1
            temp=temp.next
        is_even=False
        mid = 0
        if list_length%2==0:
            mid=list_length//2
            is_even=True 
        else :
            mid=ceil(list_length/2)
        match_array=[]
        dec_idx=-1
        start_idx=1
        temp=head
        while temp:
            if start_idx<=mid:
                match_array.append(temp.val)
                start_idx+=1
                temp=temp.next
            else:
                if not is_even:
                    dec_idx= -2
                break
        while temp:
            if temp.val != match_array[dec_idx]:
                return False
            dec_idx-=1
            temp=temp.next
        return True
        
