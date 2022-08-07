/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    private int dfs(TreeNode root){
        
        if(root==null) return 0;
        
        int left = dfs(root.left);
        int right = dfs(root.right);
        
        return (left==0 || right==0)? left+right+1 : Math.min(left,right)+1;
    }
    
    public int minDepth(TreeNode root) {
        return dfs(root);
    }
}
