class Solution {
public:
    
    bool isValidSudoku(vector<vector<char>>& board) {
        bool result = true;
        for (int i = 0; i < 9; i++)
        {
            set<char> row;
            set<char> column;
            set<char> square;
            for (int j = 0; j < 9; j++)
            {
                // Rows check
                if (board[i][j] != '.')
                {
                    if (row.find(board[i][j]) != row.end())
                        return false;
                    else
                        row.insert(board[i][j]);
                }

                // Columns check
                if (board[j][i] != '.')
                {
                   if (column.find(board[j][i]) != column.end())
                        return false;
                    else
                        column.insert(board[j][i]);
                }

                // Squares check
                int x = 3 * (i / 3) + j / 3;
                int y = 3 * (i % 3) + j % 3;
                if (board[x][y] != '.')
                {
                    if (square.find(board[x][y]) != square.end())
                        return false;
                    else
                        square.insert(board[x][y]);
                }
            }
        }
	    return true;
    }
};