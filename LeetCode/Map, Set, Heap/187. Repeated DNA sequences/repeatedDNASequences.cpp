class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string, int> map;
        set<string> ans;    // use set to eliminate duplicate answers
        
        if (s.length() >= 10)
        {
            for (int i = 0; i <= s.length() - 10; i++)
            {
                string temp = s.substr(i, 10);
                if (map.find(temp) != map.end())   // substring that occurs more than once
                {
                    ans.insert(temp);
                }
                else    // substring that occurs first time
                {
                    map[temp] = i;
                }
            }
        }

        vector<string> result(ans.begin(), ans.end());
        return result;
    }
};