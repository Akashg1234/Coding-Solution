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
    
    List<TreeNode> nodelist = new ArrayList<TreeNode>();
    
    private void inOrder(TreeNode root){
        
        if(root==null){
            return;
        }
        
        inOrder(root.left);
        nodelist.add(root);
        inOrder(root.right);
        
        //return nodelist;
    }
    
    public List<TreeNode> recoverTree(TreeNode root) {
        
        inOrder(root);
        boolean find=false;
        int len=nodelist.size();
        
        int val, first=0,second=0;
        for(int i=0; i< len ; i++){
            
            if((i >0 && (nodelist.get(i).val < nodelist.get(i-1).val)) || (i <len-1 && (nodelist.get(i).val > nodelist.get(i+1).val))){
                
                if(!find){
                    find=true;
                    first = i;
                }
                else{
                    second = i;
                }
            }
        }
        
        val=nodelist.get(first).val;
        nodelist.get(first).val=nodelist.get(second).val;
        nodelist.get(second).val=val;
        
        return nodelist;
    }
    
    
    
    
}
