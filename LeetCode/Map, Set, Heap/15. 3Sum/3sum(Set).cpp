class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        // Variables declaration
        set<vector<int>> result;
        int n = nums.size();

        // Sort the vector in ascending order
        sort(nums.begin(),nums.end());

        // Use 2 pointers to find triplets
        for(int i = 0; i < n - 2; i++)
        {
            int start = i+1;  // pointer 1
            int end = n-1;    // pointer 2
            
            while (start < end) 
            {
                if(nums[start] + nums[end] + nums[i] == 0)      // triplet found
                {
                    vector<int> triplets {nums[i],nums[start],nums[end]};
                    result.insert(triplets);
                    start++;
                    end--;
                }
                else if (nums[start] + nums[end] + nums[i] > 0)
                {
                    end--;
                }
                else
                {
                    start++;
                }
            }
        }
        
        vector<vector<int>> res(result.begin(),result.end());
        return res;
    }
};