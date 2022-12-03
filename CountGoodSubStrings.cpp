class Solution {
public:
    int countGoodSubstrings(string s) {
        int ans=0,lhs=0,rhs=0,n=s.length();
        unordered_map<char,int> map;
        while(lhs<n && rhs<n){
            map[s[rhs]]++;

            if(rhs-lhs+1<3){
                rhs++;
            }
            else if(map.size()==3){
                ans++;
                map.erase(s[lhs]);
                lhs++;rhs++;
            }
            else{
                map[s[lhs]]--;
                if(map[s[lhs]]==0){
                    map.erase(s[lhs]);
                }
                lhs++;rhs++;
            }
        }
        return ans;
    }
};
