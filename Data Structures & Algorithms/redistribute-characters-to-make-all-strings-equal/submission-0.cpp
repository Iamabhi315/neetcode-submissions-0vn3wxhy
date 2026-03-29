class Solution {
public:
    bool makeEqual(vector<string>& words) {
        unordered_map<char, int>mp;
        for(const string& word : words){
            for(char c : word){
                mp[c]++;
            }
        }
        int n = words.size();
        for(auto &p : mp) {
            if(p.second % n != 0) return false;
        }
        return true;
    }
};