// 
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0],currmax=nums[0];
        
        for(int i=1; i< nums.length; i++){
            currmax = Math.max(nums[i],currmax+nums[i]);
            maxSum = Math.max(currmax,maxSum);
        }
        return maxSum;
    }
}
