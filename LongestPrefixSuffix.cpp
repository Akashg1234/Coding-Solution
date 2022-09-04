class Solution{
  public:		
	int lps(string s) {
	    // Your code goes here
	    int n=s.length(), lPreSuf[n], lenPreSuf = 0, i=1;
	    lPreSuf[0]=0;
	    
	    while (i<n){
	        
	        if(s[i]==s[lenPreSuf]){
	            
	            lenPreSuf++;
	            lPreSuf[i]=lenPreSuf;
	            i++;
	        }
	        else{
	            if (lenPreSuf!=0){
	                
	                lenPreSuf=lPreSuf[lenPreSuf-1];
	            }
	            else{
	                
	                lPreSuf[i]=0;
	                i++;
	            }
	        }
	    }
	    return lPreSuf[n-1];
	}
};
