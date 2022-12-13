class Solution {
    public int divisorSubstrings(int num, int k) {
        int ans=0,pow = (int)Math.pow(10,k);
        for(int n=num;n>0;n/=10){
            int divisor = n%pow;
            if(divisor!=0 && num%divisor==0){
                ans++;
            }
            if(n/pow==0)
            break;
        }
        return ans;
        
    }
}
