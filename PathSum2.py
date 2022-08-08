# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,sum,ls,res):
        if root:
            if root.left==None and root.right==None and sum==root.val:
                ls.append(root.val)
                res.append(ls)
                
            self.dfs(root.left,sum-root.val,ls+[root.val],res)
            self.dfs(root.right,sum-root.val,ls+[root.val],res)
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res=[]
        self.dfs(root,targetSum,[],res)
        return res
