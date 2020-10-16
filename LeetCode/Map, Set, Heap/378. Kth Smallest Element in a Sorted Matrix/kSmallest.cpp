class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        int n = matrix.size();
	    int m = matrix[0].size();
        for (int i = 0; i < n; i++)
        {
		    for (int j = 0; j < m; j++)
            {
			    minHeap.push(matrix[i][j]);
            }
        }
        for (int i = 1; i < k; i++)
        {
            minHeap.pop();
        }
        return minHeap.top();    
    }
};