#include<vector>
#include<string>
#include<sstream>
#include<iostream>
using namespace std;
vector<string> composeRanges(vector<int> nums) {
    vector<string> result;
    if (nums.size() == 0) return result;

    int leftIndex = 0;
    for (int i = 1; i < nums.size() ; i++)
        if (nums[i] != nums[i-1] + 1)
        {
            ostringstream range;
	        range << nums[leftIndex];
            if ( i - leftIndex > 1)
            {
                range << "->" << nums[i-1];
            }
            result.push_back(range.str());
            leftIndex = i;
        }
    ostringstream range;
    range << nums[leftIndex];
    if (nums.size() - leftIndex > 1)
        range << "->" << nums[nums.size()-1];
    result.push_back(range.str());
    return result;
}

int main()
{
	vector<int> nums;
	nums.push_back(-1);
	nums.push_back(0);
	nums.push_back(1);
	nums.push_back(2);
	nums.push_back(6);
	nums.push_back(7);
	nums.push_back(9);
	vector<string> result = composeRanges(nums);
	for (int i = 0; i < result.size(); i++)
		cout << result[i] << endl;
	return 0;
}
