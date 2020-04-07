#include<iostream>
using namespace std;

int climbingStairs(int n) {
    int l[n+1];
    l[0] = 1;
    l[1] = 1;
    for (int i = 2; i <= n; i++)
        l[i] = l[i-1] + l[i-2];
    return l[n];
}

int main(){
	int n;
	cin>>n;
	cout<<climbingStairs(n);
	return 0;
}
