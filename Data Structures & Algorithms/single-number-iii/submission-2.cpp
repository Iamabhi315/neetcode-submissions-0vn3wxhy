class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
    int xr = 0;
    for(int num : nums) xr ^= num;

    int diff = xr & (-xr); // rightmost set bit

    int x = 0, y = 0;
    for(int num : nums) {
        if(num & diff) x ^= num;
        else y ^= num;
    }

    return {x, y};
}
};