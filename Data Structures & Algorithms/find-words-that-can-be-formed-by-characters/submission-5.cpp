class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        unordered_map<char,int>mp;
        for(int i = 0; i < chars.size(); i++) mp[chars[i]]++;
        int res = 0;
        for(int i=0; i < words.size(); i++)
        {
            unordered_map<char, int>temp;
            temp=mp;
            int count = 0;
            for(int j = 0; j < words[i].size(); j++)
            {
                if(temp.find(words[i][j]) != temp.end() && temp[words[i][j]] > 0)
                {
                    count++;
                    temp[words[i][j]]--;
                }
                else
                {
                    count = 0;  // ✅ char nahi mila ya exhaust — word invalid
                    break;
                }
            }
            res += count;
        }
        return res;

    }
};