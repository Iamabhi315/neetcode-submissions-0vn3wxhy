class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int mp[26] = {0};
        for (char c : chars) mp[c - 'a']++;

        int res = 0;
        for (const string& word : words) {
            int temp[26] = {0};
            for (char c : word) temp[c - 'a']++;

            bool valid = true;
            for (int i = 0; i < 26; i++) {
                if (temp[i] > mp[i]) {
                    valid = false;
                    break;
                }
            }
            if (valid) res += word.size();
        }
        return res;
    }
};