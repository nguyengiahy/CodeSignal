short toNumber(char a, char b)
{
    return (int(a) - 48) * 10 + (int(b) - 48);
}
bool inRange(short number)
{
    return (number > 0 && number < 27);
}
int mapDecoding(std::string message) {
    const int length = message.length();
    if (length == 0)
        return 1;
    if (message[0] == '0')
        return 0;
    long dp[length+1];
    dp[0] = 1; dp[1] = 1;

    for (int i = 1; i < length; i++)
    {
        short num = toNumber(message[i-1], message[i]);
        if (inRange(num))
        {
            if (num < 10)      
                dp[i+1] = dp[i];
            else if (num == 10 || num == 20)
                dp[i+1] = dp[i-1];
            else       //for 2 digits number
                dp[i+1] = dp[i-1] + dp[i];
        }
        else 
        {
            if (message[i] == '0')
                return 0;
            else
                dp[i+1] = dp[i];
        }
    }    

    long mod = 1e9+7;
    return dp[length] % mod;
}
