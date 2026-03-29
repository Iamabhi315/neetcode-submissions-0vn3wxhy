class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_map<char, bool>mp;
        for(int i = 0; i < allowed.size(); i++)
        {
            if(mp.find(allowed[i]) == mp.end()) mp[allowed[i]] = true;
        }
        int count=0;
        bool valid = false;
        for(int i = 0; i < words.size(); i++)
        {
            for(int j = 0; j < words[i].size(); j++)
            {
                if(mp.find(words[i][j]) != mp.end())
                    valid = true;
                else
                {
                    valid = false;
                    break;
                }
            }
            if(valid) count++;
        }
        return count;
    }
};