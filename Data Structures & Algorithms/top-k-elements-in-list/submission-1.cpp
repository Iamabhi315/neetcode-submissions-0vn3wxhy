class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map<int, int> mp;

        
        for(int x : nums) mp[x]++;

    
        sort(nums.begin(), nums.end(), [&](int a, int b){
            if(mp[a] == mp[b]){
                return a > b;  // value descending
            }
            return mp[a] < mp[b]; // freq ascending
        });
        int i = 0;
        int n = nums.size();
        vector<int>res;
        while(k>0){
            res.push_back(nums[n-1-i]);
            i += mp[nums[n-1-i]];
            k--;
        }
        return res;

    }
};
