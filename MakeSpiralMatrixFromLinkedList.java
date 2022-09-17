/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        
        int matrix[][] =new int[m][n];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                matrix[i][j]=-1;
            }
        }
        
        int right=n-1,left=0,top=0,down=m-1,direction=1;
        
        ListNode temp=head;
        
        while(left <= right && top<=down && temp!=null){
            
            if(direction==1){
                for(int i=left;i<=right && temp!=null;i++){
                    matrix[top][i]=temp.val;
                    temp=temp.next;
                }
                top++;
                direction=2;
            }
            
            if(direction==2){
                for(int i=top;i<=down && temp!=null;i++){
                    matrix[i][right]=temp.val;
                    temp=temp.next;
                }
                right--;
                direction=3;
            }
            
            if(direction==3){
                for(int i=right;i>=left && temp!=null;i--){
                    matrix[down][i]=temp.val;
                    temp=temp.next;
                }
                down--;
                direction=4;
            }
            
            if(direction==4){
                for(int i=down;i>=top && temp!=null;i--){
                    matrix[i][left]=temp.val;
                    temp=temp.next;
                }
                left++;
                direction=1;
            }
        }
        return matrix;
    }
}
