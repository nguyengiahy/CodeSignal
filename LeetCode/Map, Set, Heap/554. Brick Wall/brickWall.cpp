class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int, int> cut;
        int maxCut = 0;
        
        for (int i = 0; i < wall.size(); i++)
        {
            int count = 0;
            for (int j = 0; j < wall[i].size() - 1; j++)
            {
                count += wall[i][j];
                cut[count]++;
                if (cut[count] > maxCut)
                    maxCut = cut[count];
            }
        }
        
        return wall.size() - maxCut;
    }
};