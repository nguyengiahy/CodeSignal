void swap(int& a, int& b)
{
    int temp = a;
    a = b;
    b = temp;
}
std::vector<std::vector<int>> rotateImage(std::vector<std::vector<int>> a) {
    int n = a.size();
    for (int i = 0; i < n; i++)
        for (int j = i; j < n; j++)
		swap(a[i][j],a[j][i];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n/2; j++)
		swap(a[i][j],a[i][n-j-1];
    return a;
}
