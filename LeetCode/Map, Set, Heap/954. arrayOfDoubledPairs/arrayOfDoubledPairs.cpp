class Solution {
public:
    bool canReorderDoubled(vector<int>& A) {
        unordered_map<int, int> frequencies;
        sort(A.begin(), A.end());
        for (int i = 0; i < A.size(); i++)
        {
            frequencies[A[i]]++;
        }
        
        for (int i = 0; i < A.size(); i++)
        {
            if (frequencies[A[i]] > 0)
            {
                int temp;
                if (A[i] > 0)
                    temp = 2 * A[i];
                else if (A[i] % 2 == 0)
                    temp = A[i] / 2;
                else
                    return false;
                if (frequencies[temp] > 0)
                {
                    frequencies[A[i]]--;
                    frequencies[temp]--;
                }
                else
                {
                    return false;    
                }
            }
        }
        return true;
    }
};