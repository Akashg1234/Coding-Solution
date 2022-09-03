class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1:
            return s
        
        res_arr = [""]*min(numRows,len(s))
        
        curr_row=0
        
        goingDown = False
        
        for c in s:
            res_arr[curr_row]+=c
            
            if (curr_row==0 or curr_row==(numRows-1)):
                goingDown = not goingDown
                
            curr_row+= 1 if goingDown else -1
            
        return ''.join(res_arr)
        
        
