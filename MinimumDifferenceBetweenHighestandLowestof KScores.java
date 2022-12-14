class Solution {
    public int minimumDifference(int[] nums, int k) {
        int res=Integer.MAX_VALUE,n=nums.length;
        Arrays.sort(nums);
        for(int i=k-1;i<n;i++){
            res = (int)Math.min(res,nums[i]-nums[i-k+1]);
        }
        return res;
    }
}
