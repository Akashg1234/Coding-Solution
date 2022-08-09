# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res=0
    
    def dfs(self,root,currsum):
        
        if root == None:
            return 
        currsum  = currsum*10+root.val
        if root.left==None and root.right==None:
            self.res+=currsum
            return 
        
        self.dfs(root.left,currsum)
        self.dfs(root.right,currsum)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if root.left==None and root.right==None:
            self.res+=root.val
        self.dfs(root.left,root.val)
        self.dfs(root.right,root.val)
        return (self.res)
