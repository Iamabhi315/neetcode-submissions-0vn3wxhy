class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, bool>mp;
        for(int i = 0; i < nums1.size(); i++){
            if(mp.find(nums1[i]) == mp.end()) mp[nums1[i]] = true;
        }
        vector<int>res;
        for(int i = 0; i < nums2.size(); i++){
            if(mp[nums2[i]] == true){
                res.push_back(nums2[i]);
                mp.erase(nums2[i]);
            }
        }
        return res;
    }
};