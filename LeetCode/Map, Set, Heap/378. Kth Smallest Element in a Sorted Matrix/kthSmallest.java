class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int m = matrix[0].length;
        
        PriorityQueue<Integer> minHeap = new PriorityQueue(n*m);
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                minHeap.add(matrix[i][j]);
            }
        }
        
        for (int i = 0; i < k-1; i++){
            minHeap.poll();
        }
        
        return minHeap.poll();
    }
}