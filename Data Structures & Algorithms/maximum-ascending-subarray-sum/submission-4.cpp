class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int sum=nums[0];
        int result=nums[0];
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]<nums[i+1]){
                sum+=nums[i+1];
                result=max(sum,result);
            }
            else{
                sum=nums[i+1];
            }
        }
        return result;
        
    }
};