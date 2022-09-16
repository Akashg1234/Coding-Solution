class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        maxSum=0
		temp=head
		listlen=0

        while temp:
            temp=temp.next
			listlen+=1   
			
        mid = listlen//2
		listlen=0
		temp=head
		stack = []
		
        while listlen<mid:
            stack.append(temp.val)
			listlen+=1
			temp=temp.next
            
        while temp:
            currval=stack.pop()
			currsum = currval+temp.val
			maxSum = max(maxSum,currsum)
			temp=temp.next
            
        return maxSum
