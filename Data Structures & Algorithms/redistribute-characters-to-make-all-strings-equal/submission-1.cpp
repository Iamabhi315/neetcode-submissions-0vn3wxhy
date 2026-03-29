class Solution {
public:
    bool makeEqual(vector<string>& words) {
        vector<int> counts(26, 0);
        int n = words.size();
        for (const string& word : words) {
            for (char c : word) {
                counts[c - 'a']++;
            }
        }
        for (int i = 0; i < 26; i++) {
            if (counts[i] % n != 0) {
                return false;
            }
        }
        
        return true;
    }
};