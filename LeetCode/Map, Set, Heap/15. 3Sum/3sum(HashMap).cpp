class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // Variables
        unordered_map<int, int> map;
        vector<vector<int>> result;
        int n = nums.size();

        // Sort the inputs
        sort(nums.begin(), nums.end());

        // Add key-value pairs
        for (int i = 0; i < n; i++)
        {
            map[nums[i]] = i;
        }

        // Find triplets
        for (int i = 0; i < n;)
        {
            for (int j = i+1; j < n;)
            {
                int c = -nums[i] - nums[j];
                // If key c exists, and index of that element > j (to avoid duplicates), then accept the triplet.
                if (map.find(c) != map.end() && map[c] > j)
                {
                    vector<int> triplet = { nums[i], nums[j], c };
                    result.push_back(triplet);
                }

                int temp = nums[j];
                while (j < n && nums[j] == temp)	// Avoid duplicates
                {
                    j++;
                }
            }

            int temp = nums[i];
            while (i < n && nums[i] == temp)	// Avoid duplicates
            {
                i++;
            }
        }

        return result;
    }
};