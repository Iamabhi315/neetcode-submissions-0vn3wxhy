class Solution {
public:
    char findTheDifference(string s, string t) {
        vector<int>temp1(26,0);
        vector<int>temp2(26,0);
        for(int i = 0; i < s.size(); i++){
            temp1[s[i] - 'a']++;

        }
        for(int i = 0; i < t.size(); i++){
            temp2[t[i] - 'a']++;
        }
        char res;
        for(int i = 0; i < t.size(); i++){
            if(temp1[t[i] - 'a'] < temp2[t[i] - 'a']) res=t[i];
        }
        return res;
    }
};