class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker)     {
        vector<pair<int,int>> jobs;
        for (int i = 0; i < profit.size(); i++)
        {
            jobs.push_back({difficulty[i], profit[i]});
        }
        
        sort(jobs.begin(), jobs.end());
        sort(worker.begin(), worker.end());
        
        int j = 0, maxPreProfit = 0, res = 0;
        for (int i = 0; i < worker.size(); i++)
        {
            while (j < profit.size() and jobs[j].first <= worker[i])
            {
                maxPreProfit = max(maxPreProfit, jobs[j].second);
                j++;
            }
            res += maxPreProfit;
        }
        
        return res;
    }
};