class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        vector<int> nextState(8);
        set<vector<int>> set;
        bool flag = false;  // true if the cycle finishes

        for (int i = 0; i < N; i++)
        {
            for (int j = 1; j < 7; j++)
            {
                nextState[j] = cells[j - 1] == cells[j + 1] ? 1 : 0;
            }
            if (set.find(nextState) != set.end())	// cycle finishes
            {
                flag = true;
                break;
            }
            set.insert(nextState);
            cells = nextState;
        }

        if (flag)
        {
            N = N % set.size();
            for (int i = 0; i < N; i++)
            {
                for (int j = 1; j < 7; j++)
                {
                    nextState[j] = cells[j - 1] == cells[j + 1] ? 1 : 0;
                }
                cells = nextState;
            }
        }
        return cells;
    }
};