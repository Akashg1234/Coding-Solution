class Solution {
    public int minimumRecolors(String blocks, int k) {
        int win = 0;
        int start = 0;
        int end = k;
        int min = Integer.MAX_VALUE;
        for(int i = 0 ; i < k; i++){
            if(blocks.charAt(i) == 'W'){
                win++;
            }
        }
        
        if(win < min){
            min = win;
        }
        // System.out.print(min);
        while(end < blocks.length()){
            if(blocks.charAt(start) == 'W'){
                win--;
            }
            if(blocks.charAt(end) == 'W'){
                win++;
            }
            if(win < min){
                min = win;
            }
            start++;
            end++;
        }
        return min; 
    }
}
