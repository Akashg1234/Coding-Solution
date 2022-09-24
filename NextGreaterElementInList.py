# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        ans,stack,index,temp=[],[],0,head
        
        while temp:
            ans.append(0)
            currentval=temp.val
            
            while stack and stack[-1][0]<currentval:
                last_value = stack.pop()
                ans[last_value[1]] = currentval
                
            stack.append((currentval,index))
            index+=1
            temp=temp.next
            
        return ans
        
