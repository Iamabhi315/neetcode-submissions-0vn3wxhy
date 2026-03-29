class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n=nums.size();
        vector<int>result;
        for(int i=0;i<n;i++){
            int temp=abs(nums[i])-1;
            if(nums[temp]>0)
            nums[temp]=-nums[temp];
        }
        for(int i=0;i<n;i++){
            if(nums[i]>0) result.push_back(i+1);
        }
        return result;
    }
};