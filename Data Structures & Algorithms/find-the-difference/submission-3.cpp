class Solution {
public:
    char findTheDifference(string s, string t) {
        int sumS=0;
        for(int i=0;i<s.length();i++){
            sumS+=s[i];

        }

        int sumT=0;
        for(int i=0;i<t.length();i++){
            sumT+=t[i];

        }

        char ans=static_cast<char>(sumT-sumS);
        return ans;
        
        
    }
};