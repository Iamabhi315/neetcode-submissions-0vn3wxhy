class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_set<char> allowed_set(allowed.begin(), allowed.end());
        int count=0;
        bool valid = false;
        for(const string& word : words) {
            bool valid = true;
            for(char c : word) {
                if(!allowed_set.count(c)) { valid = false; break; }
            }
            if(valid) count++;
        }
        return count;
    }
};