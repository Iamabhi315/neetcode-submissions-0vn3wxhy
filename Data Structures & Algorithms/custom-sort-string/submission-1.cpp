class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> freq(26, 0);

        // Step 1: Count frequency
        for(char c : s) {
            freq[c - 'a']++;
        }

        string res;

        for(char c : order) {
            while(freq[c - 'a'] > 0) {
                res.push_back(c);
                freq[c - 'a']--; 
            }
        }

        for(int i = 0; i < 26; i++) {
            while(freq[i] > 0) {
                res.push_back(i + 'a');
                freq[i]--; 
            }
        }

        return res;
    }
};