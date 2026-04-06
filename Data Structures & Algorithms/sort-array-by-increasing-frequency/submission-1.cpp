class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        map<int, int> mp;

        
        for(int x : nums) mp[x]++;

    
        sort(nums.begin(), nums.end(), [&](int a, int b){
            if(mp[a] == mp[b]){
                return a > b;  // value descending
            }
            return mp[a] < mp[b]; // freq ascending
        });

        return nums;
    }
};