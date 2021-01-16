class Solution {
public:
    string getHint(string secret, string guess) {
        int a = 0, b = 0;
        vector<int> check;
        unordered_map<char, int> frequencies;
        
        for (int i = 0; i < secret.length(); i++)
        {
            if (secret[i] == guess[i])  
            {
                a++;    // increase bulls 
                check.push_back(1);     // flag the index
            }
            else
            {
                frequencies[secret[i]]++;
                check.push_back(0);     
            }
        }
        
        for (int i = 0; i < secret.length(); i++)
        {
            if (check[i] == 0)
            {
                if (frequencies[guess[i]] > 0)
                {
                    b++;
                    frequencies[guess[i]]--;
                }
            }
        }
        
        string result = to_string(a) + "A" + to_string(b) + "B";
        return result;
    }
};