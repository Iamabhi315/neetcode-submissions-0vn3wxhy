class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int>ans;
        unordered_map<int,int>m;

        for(auto &a:nums)m[a]++;

        for(auto &a:m){
            if(a.second == 1){
                ans.push_back(a.first);
            }
        }

        return ans;
    }
};