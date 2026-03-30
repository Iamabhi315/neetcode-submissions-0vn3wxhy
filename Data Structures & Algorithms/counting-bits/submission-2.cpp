class Solution {
public:
    vector<int> countBits(int n) {
        vector<int>v(n+1,0);
        for(int i=1; i<=n; i++){
            //v[i]=(i&1) + v[i/2];
            v[i] = v[i & (i - 1)] + 1;
        }
        return v;
    }
};
