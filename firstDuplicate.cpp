int firstDuplicate(std::vector<int> a) {
    int answer[100000] = {0};
    int pos = 0;
    for (int i = 0; i < a.size(); i++)
    {
        answer[a[i]]++;
        if (answer[a[i]] == 2)
            return a[i];
    }
    return -1;
}
