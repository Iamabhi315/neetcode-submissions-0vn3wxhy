class Solution {
public:
    string largestGoodInteger(string num) {
        
        char temp = num[0];
        int count = 1;
        int check = 0;
        string res = "";

        for(int i = 1; i<num.size(); i++)
        {
            if(temp == num[i]) count++;
            else count=1;
            if(count==3 && (temp - '0') >= check)
            {
                check = temp - '0';
                res = string(1, temp);
            }
            temp = num[i];
        }
        return res + res + res;
        
    }
};