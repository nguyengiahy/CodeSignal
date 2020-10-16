class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int n = bloomDay.size();
        int ans = -1;
        if (m*k > n)
            return -1;
        
        // Find max day and min day
        int minDay = INT_MAX;
        int maxDay = INT_MIN;
        for  (int i = 0; i < n; i++)
        {
            minDay = min(minDay, bloomDay[i]);
            maxDay = max(maxDay, bloomDay[i]);
        }
        
        // Binary search
        while (minDay <= maxDay)
        {
            int mid = (minDay + maxDay) / 2;
            int count = 0;
            int out = 0;
            for (int i = 0; i < n; i++)
            {
                if (bloomDay[i] <= mid)
                {
                    if (count == 0)
                        count++;
                    else if (bloomDay[i-1] <= mid)
                        count++;
                    
                    if (count == k)
                    {
                        out++;
                        count = 0;
                    }
                }
                else
                {
                    count = 0;
                }
            }
            
            if (out < m)
            {
                minDay = mid + 1;
            }
            else
            {
                ans = mid;
                maxDay = mid - 1;
            }
        }
        return ans;
    }
    
};