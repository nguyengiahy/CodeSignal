#include <sstream>
#include <string.h>

//Map a letter into corresponding number
char lookup(char ch, std::vector<std::vector<char>> solution)
{
    for (int i = 0; i < solution.size(); i++)
    {
        if (ch == solution[i][0])
            return solution[i][1];
    }
    return -1;
}

//Map a letter string into number string
string mapToString(string s, std::vector<std::vector<char>> solution)
{
    string result = "";
    for (int i = 0; i < s.length(); i++)
        result += lookup(s[i], solution);
    return result;
}

//Return number of digits of an integer
int numberOfDigits(unsigned long long int a)
{
    if (a < 10)
        return 1;
    int result = 0;
    while (a > 0)
    { 
        a = a/10;
        result++;        
    }
    return result;
}

//Convert a string to number
unsigned long long int convertToInt(string s)
{
    stringstream geek(s);
    unsigned long long int result;
    geek >> result;

    //Check if there is leading zeros
    if (numberOfDigits(result) != s.length())
        return -1;
    
    return result;
}
bool isCryptSolution(std::vector<std::string> crypt, std::vector<std::vector<char>> solution) {
    int word1, word2, word3;
    word1 = convertToInt( mapToString(crypt[0], solution) );
    word2 = convertToInt( mapToString(crypt[1], solution) );
    word3 = convertToInt( mapToString(crypt[2], solution) );
    
    return word3 == word1 + word2;
}

