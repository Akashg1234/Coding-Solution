class Solution {
    public String longestNiceSubstring(String s) {
        if (s.length()<2)return "";
        
        char []cArr = s.toCharArray();
        
        HashSet <Character> set = new HashSet<>();
        
        for(char c:cArr) set.add(c);
        
       //System.out.println("{S: "+s+" i: "+it+"\n"+" set: "+set+"\n"+"}\n");
        
        
        for(int i=0;i<cArr.length;i++){
            char c = cArr[i];
            
            if(set.contains(Character.toUpperCase(c)) && set.contains(Character.toLowerCase(c))){
                continue;
            }
            
            String subString1 = longestNiceSubstring(s.substring(0,i));
            String subString2 = longestNiceSubstring(s.substring(i+1));
            //System.out.println("{i: "+it+" Sub1: "+subString1+" Sub2: "+subString2+"}\n");
            return subString1.length()>=subString2.length() ? subString1 : subString2;
        }
        return s;
    }
}
