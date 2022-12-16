class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double maxVal = Double.MIN_VALUE,sum=0;
        int n=nums.length;
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }

        maxVal = sum;

        for(int i=k;i<n;i++){
            sum+= nums[i]-nums[i-k];
            maxVal = Math.max(maxVal,sum);
        }

        return maxVal/k;
    }
}
