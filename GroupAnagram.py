class Solution:
    def groupAnagrams(self, strs):
        ans = []
        
        resultant = []
        
        for s in strs:
            
            val = sorted(s)
            
            if val in resultant:
                #print(resltant.index(val))
                ans[resultant.index(val)].append(s)
                
            elif val not in resultant:
                resultant.append(val)
                ans.append([s])
                
        return ans
        
