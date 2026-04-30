class Solution {
public:

    string encode(vector<string>& strs) {
        string res="";
        for(auto x : strs){
            res += to_string(x.size()) + "#" + x;
        }
        return res;
}
        

    vector<string> decode(string s) {
        vector<string>res;
        int i=0,n=s.size();
        while(i<n){
            int j=i;
            while(s[j] != '#')
                j++;
            int length = stoi(s.substr(i, j-i));
            res.push_back(s.substr(j+1,length));
            i = j + 1 + length;
        }
        return res;
    }
};
