# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root,minimum,maximum):
            
            if not root:
                return True
            
            val=root.val
            
            if maximum<= val or val <=minimum:
                return False
            
            left = -float("inf")
            right = float("inf")
            
            if root.left:
                left=root.left.val
            if root.right:
                right=root.right.val
            
            if left<val and right>val:
                return all([valid(root.left,minimum,val),valid(root.right,val,maximum)])
            return False
        return valid(root,-float("inf"),float("inf"))
        
