char firstNotRepeatingCharacter(std::string s) {
    int pos = 26;
    int occurence[26] = {0};
    for (int i = 0; i < s.length(); i++)
    {
        int index = int(s[i]) - 97; 
        occurence[index]++;
    }
    for (int i = 0; i < s.length(); i++)
    {
        int index = int(s[i]) - 97; 
        if (occurence[index] == 1)
            return s[i];
    }
    return '_';
}

