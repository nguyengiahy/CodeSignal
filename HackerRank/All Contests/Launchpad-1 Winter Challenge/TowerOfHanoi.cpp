#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void solve(int n, string start, string middle, string target)
{
    if (n>0)
    {
        solve(n-1,start,target,middle);
        cout<<"Moving ring " << n << " from " << start << " to " << target << endl;
        solve(n-1,middle,start,target);
    }
}
int main() {
    int n;
    cin>>n;
    solve(n,"A","C","B");
    return 0;
}
