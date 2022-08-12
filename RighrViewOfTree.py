# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,ls,last_level,currlevel):
        if not root:
            return
        
        if last_level[0]<currlevel:
            ls.append(root.val)
            last_level[0]=currlevel
            
        self.dfs(root.right,ls,last_level,currlevel+1)
        self.dfs(root.left,ls,last_level,currlevel+1)
        
        return
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        currlevel=1
        last_level=[0]
        
        self.dfs(root,ls,last_level,currlevel)
        return ls
        
  
