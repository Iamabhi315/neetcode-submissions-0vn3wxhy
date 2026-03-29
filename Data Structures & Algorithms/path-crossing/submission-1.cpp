class Solution {
public:
    bool isPathCrossing(string path) {
        int x = 0, y = 0;
        unordered_set<long long> st;

        long long key = 0; // (0,0)
        st.insert(key);

        for(char c : path) {
            if(c == 'N') y++;
            else if(c == 'S') y--;
            else if(c == 'E') x++;
            else x--;

            long long key = (long long)x * 1000000 + y;

            if(st.count(key)) return true;

            st.insert(key);
        }
        return false;
    }
};