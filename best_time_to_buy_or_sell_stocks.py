class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        min_index=0
        min_val=prices[0]
        
        for i in range(1,len(prices)):
            
            if prices[i]<min_val:
                min_val = prices[i]
                min_index = i
                
        max_val= prices[min_index] 
        
        for j in range(min_index,len(prices)):
            
            if prices[j]>max_val:
                max_val = prices[j]
                
        return max_val-min_val
