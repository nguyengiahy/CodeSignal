#include<iostream>
#include<vector>
using namespace std;

int houseRobber(std::vector<int> nums) {
    int n = nums.size();
    if (n == 0)
        return 0;
    else if (n == 1)
        return nums[0];
    int dp[n];
    dp[0] = nums[0];
    dp[1] = max(nums[0], nums[1]);
    for (int i = 2;  i <= n-1; i++)
        dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
    return dp[n-1];
}

int main()
{
	vector<int> a;
	int n,x;
	cout<<"Length of the input: ";
	cin>>n;
	for (int i = 0; i < n; i++)
	{
		cout<< "Enter value for " << i+1 <<" element:";
		cin>>x;
		a.push_back(x);
	}
	cout<<houseRobber(a);
	return 0;
}
