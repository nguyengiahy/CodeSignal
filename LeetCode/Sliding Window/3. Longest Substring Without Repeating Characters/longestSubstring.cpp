class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() <= 1)
            return s.length();
        
        int start = 0, end = 0, result = 0;
        unordered_map<char, int> frequencies;

        while (end < s.length())
        {
            result = max(result, end-start);
            if (frequencies[s[end]] > 0)    //this char is already in the subarray
            {
                frequencies[s[start]]--;
                start++;
            }
            else if (end < s.length() && frequencies[s[end]] == 0)
            {
                frequencies[s[end]]++;
                end++;
            }
            result = max(result, end-start);
        } 
        return result;
    }
};