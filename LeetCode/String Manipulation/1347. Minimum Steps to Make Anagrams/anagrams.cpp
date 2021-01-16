class Solution {
public:
    int minSteps(string s, string t) {
        int frequencies[26] = {0};
        int result = 0;
        
        for (int i = 0; i < s.length(); i++)
            frequencies[s[i] - 'a']++;
        
        for (int i = 0; i < t.length(); i++)
            if (frequencies[t[i] - 'a']>0)
                frequencies[t[i] - 'a']--;
        
        for (int i = 'a'; i <= 'z'; i++)
            result += frequencies[i - 'a'];            
        
        return result;
    }
};