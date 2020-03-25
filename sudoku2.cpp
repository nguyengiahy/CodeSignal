#include<iostream>
#include<vector>
#define n 9
using namespace std;

//get input
vector< vector<char> > getInput()
{
	vector< vector<char> > grid;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin>>grid[i][j];
	return grid;
}

//Check for rows
bool checkHorizontal(vector< vector<char> > grid)
{
	for (int i = 0; i < n; i++)
    {
        int checkArray[10] = {0};
        for (int j = 0; j < n; j++)
            if (grid[i][j] != '.')
            {
                int toNumber = int(grid[i][j]) - 48;
                checkArray[toNumber]++;
                if (checkArray[toNumber] == 2)
                    return false;
            }
    }
    return true;
}

//check for columns
bool checkVertical(vector< vector<char> > grid)
{
	for (int j = 0; j < n; j++)
    {
        int checkArray[10] = {0};
        for (int i = 0; i < n; i++)
        {
            if (grid[i][j] != '.')
            {
                int toNumber = int(grid[i][j]) - 48;
                checkArray[toNumber]++;
                if (checkArray[toNumber] == 2)
                    return false;
            }
        }
    }
    return true;
}

//check for sub-grid
bool checkSubGrid(vector< vector<char> > grid)
{
	for(int i = 0; i < 3; i++) 
        for(int j = 0; j < 3; j++) 
        {
            int checkArray[10] = {0};
            for(int k = 0; k < 3; k++) 
                for(int m = 0; m < 3; m++) 
                {
                    int x = i*3+k;
                    int y = j*3+m;
                    if (grid[x][y] != '.')
                    {
                        int toNumber = int(grid[x][y]) - 48;
                        checkArray[toNumber]++;
                        if (checkArray[toNumber] == 2)
                            return false;
                    }
                }
        }
    return true;
}

bool sudoku2(vector< vector<char> > grid) {
    //Check horizontal
    bool rows = checkHorizontal(grid);
    //Check vertical
    bool columns = checkVertical(grid);
    //Check sub-grids
    bool subGrid = checkSubGrid(grid);
    return (rows && columns && subGrid);
}

int main()
{
	vector< vector<char> > grid = getInput();
	cout<< sudoku2(grid);
	return 0;
}

