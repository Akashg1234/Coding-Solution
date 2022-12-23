class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int sum=0,ans=0,n=arr.length;
        for(int i=0;i<k;i++){
            sum+=arr[i];
        }
        int avg=sum/k;
        if(avg>=threshold)ans++;

        for(int i=k;i<n;i++){
            sum+=arr[i]-arr[i-k];
            avg=sum/k;
            if(avg>=threshold)ans++;
        }
        return ans;
    }
}
