class Solution {
public:
    bool isPathCrossing(string path) {
        int x = 0, y = 0;
        unordered_map<string, bool> mp;

        mp["0,0"] = true;

        for(int i = 0; i < path.size(); i++) {
            if(path[i] == 'N') y++;
            else if(path[i] == 'S') y--;
            else if(path[i] == 'E') x++;
            else x--;

            string key = to_string(x) + "," + to_string(y);

            if(mp.find(key) != mp.end())
                return true;

            mp[key] = true;
        }
        return false;
    }
};