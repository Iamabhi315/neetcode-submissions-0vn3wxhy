class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> res;
        res.push_back({1});

        for (int i = 1; i <= rowIndex; i++) {  

            vector<int> temp;

            for (int j = 0; j < i + 1; j++) {  

                if (j == 0 || j == i)           
                    temp.push_back(1);
                else
                    temp.push_back(res[i-1][j-1] + res[i-1][j]);  
            }

            res.push_back(temp);
        }

        return res[rowIndex];
    }
};