class Solution {
public:
    int maxDifference(string s) {
        unordered_map<char,int> mp;

        for(char ch : s) {
            mp[ch]++;
        }

        int maxOdd = INT_MIN;
        int minEven = INT_MAX;

        for(auto x : mp) {
            if(x.second % 2 == 1) {   // odd
                maxOdd = max(maxOdd, x.second);
            }
            else {                    // even
                minEven = min(minEven, x.second);
            }
        }

        if(maxOdd == INT_MIN || minEven == INT_MAX)
            return -1;  // no valid pair

        return maxOdd - minEven;
    }
};