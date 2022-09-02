class Solution:
    numrange=range(0,10)
    
    def clamp(self,n,smallest=-2**31,highest=2**31-1):
        return max(smallest,min(n,highest))
    
    def myAtoi(self, s: str) -> int:
        
        s=s.strip()
        
        n = len(s)
        
        if n==0:
            return 0
        
        minus = False
        
        startIdx=0
        
        res=0
        
        if s[0]=='-':
            minus = True
            startIdx=1
            
        elif s[0]=='+':
            startIdx=1
            
        for idx in range(startIdx,n):
            try:
                value= int(s[idx])
            except:
                break
            
            if value in self.numrange:
                res = res*10+value
            else:
                break
            
        if minus:return self.clamp(-1*res)
        else:return self.clamp(res)
        
