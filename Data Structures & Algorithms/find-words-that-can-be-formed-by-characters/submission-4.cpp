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
                if(temp.find(words[i][j]) == temp.end())
                {
                    count=0;
                    break;
                }
                if(temp.find(words[i][j]) != temp.end())
                {
                    if(temp[words[i][j]]<=0) break;
                     count++;
                     temp[words[i][j]]--;
                }
            }
            if(words[i].size()==count)
            res += count;
        }
        return res;

    }
};