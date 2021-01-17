class Solution {
public:
    
    bool isValidSudoku(vector<vector<char>>& board) {
        bool result = true;
        for (int i = 0; i < 9; i++)
        {
            unordered_map<char, bool> row;
            unordered_map<char, bool> column;
            unordered_map<char, bool> square;
            for (int j = 0; j < 9; j++)
            {
                // Rows check
                if (board[i][j] != '.')
                {
                    if (row.find(board[i][j]) != row.end())
                        return false;
                    else
                        row[board[i][j]] = true;
                }

                // Columns check
                if (board[j][i] != '.')
                {
                   if (column.find(board[j][i]) != column.end())
                        return false;
                    else
                        column[board[j][i]] = true;
                }

                // Squares check
                int x = 3 * (i / 3) + j / 3;
                int y = 3 * (i % 3) + j % 3;
                if (board[x][y] != '.')
                {
                    if (square.find(board[x][y]) != square.end())
                        return false;
                    else
                        square[board[x][y]] = true;
                }
            }
        }
	    return true;
    }
};