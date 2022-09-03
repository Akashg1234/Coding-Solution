class Solution:
    close_brac = [')','}',']']
    open_brac = ['(','{','[']
    
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            
            if c in self.open_brac:
                stack.append(c)
                
            else:
                if not stack:
                    return False
                curr_char = stack.pop()
                
                if self.close_brac.index(c) != self.open_brac.index(curr_char):
                    return False
        
        if stack:
            return False
        
        return True
        
