class Solution:
    
    low=0
    maxlen=0
    
    def checkPalindrom(self,s,j,k,n):
        while(j>=0 and k<n and s[j]==s[k]):
            j-=1
            k+=1
            #print()
        
        if self.maxlen<k-j-1:
            self.low=j+1
            self.maxlen=k-j-1
            
    def longestPalindrome(self, s: str) -> str:
        
        n=len(s)
        
        if n<2:
            return s
        
        for i in range(n-1):
            self.checkPalindrom(s,i,i,n)
            self.checkPalindrom(s,i,i+1,n)
            
        return s[self.low:self.low+self.maxlen]
