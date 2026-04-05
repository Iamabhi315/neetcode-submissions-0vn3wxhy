class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> mp;

        // Step 1: frequency count
        for(int x : nums) mp[x]++;

        // Step 2: sort nums directly
        sort(nums.begin(), nums.end(), [&](int a, int b){
            if(mp[a] == mp[b]){
                return a > b;  // value descending
            }
            return mp[a] < mp[b]; // freq ascending
        });

        return nums;
    }
};