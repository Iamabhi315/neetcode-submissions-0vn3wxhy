class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> st;
        
        for(string email : emails){
            string local = "", domain = "";
            int i = 0;
            
            while(email[i] != '@'){
                if(email[i] == '.') {
                    i++;
                    continue;
                }
                
                if(email[i] == '+'){
                    while(email[i] != '@') i++;
                    break;
                }
                
                local += email[i];
                i++;
            }
            
            domain = email.substr(i);
            st.insert(local + domain);
        }
        
        return st.size();
    }
};