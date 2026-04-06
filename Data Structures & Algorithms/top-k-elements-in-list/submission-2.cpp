class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(int x : nums) mp[x]++;

        vector<vector<int>> bucket(nums.size() + 1);

        for(auto &p : mp) {
            bucket[p.second].push_back(p.first);
        }

        vector<int> res;

        for(int i = nums.size(); i >= 0 && k > 0; i--) {
            for(int x : bucket[i]) {
                res.push_back(x);
                k--;
                if(k == 0) break;
            }
        }

        return res;
    }
};