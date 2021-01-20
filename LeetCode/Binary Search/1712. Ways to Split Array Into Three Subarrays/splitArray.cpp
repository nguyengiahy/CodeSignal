/* 
preSum[left] <= preSum[mid] - preSum[left] <= preSum[right] - preSum[mid]
=> 2preSum[left] <= preSum[mid] <= (preSum[right] + preSum[left]) / 2
*/

class Solution {
public:
    // Binary search for lower index
    int lower(int left, int right, vector<int>& preSum)
    {
        int i = left - 1;
        int ans = -1;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (preSum[mid] >= 2*preSum[i])
            {
                ans = mid;
                right = mid - 1;
            }
            else
                left = mid + 1;
        }
        return ans;
    }
    
    // Binary search for upper index
    int upper(int left, int right, vector<int>& preSum)
    {
        int i = left - 1;
        int ans = -1;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (preSum[mid] <= (preSum[i] + preSum[preSum.size() - 1])/2)
            {
                ans = mid;
                left = mid + 1;
            }
            else
                right = mid - 1;
        }
        return ans;
    }
    
    
    int waysToSplit(vector<int>& nums) {
        int n = nums.size();
        long long result = 0;
        
        // Calculate preSum vector
        vector<int> preSum;
        preSum.push_back(nums[0]);
        for (int i = 1 ; i < n; i++)
        {
            preSum.push_back(preSum[i-1] + nums[i]);
        }
        
        // Solve
        for (int i = 0; i < n - 2; i++)	
        {
        	//Because the indices are i, j, k => j index must be <= n - 2
            int left_index = lower(i+1, n-2, preSum);
            int right_index = upper(i+1, n-2, preSum);
            if (left_index == -1 || right_index == -1 || left_index > right_index)
                continue;
            result += (right_index - left_index + 1);
        }
        
        return result % (int)(1e9+7);
    }
};