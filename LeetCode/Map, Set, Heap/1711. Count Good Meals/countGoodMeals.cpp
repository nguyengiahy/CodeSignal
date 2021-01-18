class Solution {
public:
    int countPairs(vector<int>& deliciousness) {
        unordered_map<int, int> frequencies;
        int result = 0, mod = 1e9 + 7;
        
        for (int i = 0; i < deliciousness.size(); i++)
            frequencies[deliciousness[i]]++;
        
        for (int i = 0; i < deliciousness.size(); i++)
        {
            frequencies[deliciousness[i]]--;

            int j = 0;
            while (j <= 21)    
            {
                int diff = pow(2,j) - deliciousness[i];
                if (frequencies[diff])
                {
                    result += frequencies[diff];
                    result %= mod;
                }
                j++;
            }
        }
        
        return result;
    }
};