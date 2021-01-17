class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        string result = "";
        
        // Handle negative result
        if ((long)numerator * denominator < 0)
            result += "-";
        
        // Convert to long type
        long divisor = (long)abs(numerator);
        long dividend = (long)abs(denominator);
        long remainder = divisor % dividend;
        
        result += to_string(divisor / dividend);
        
        // If there is no floating point
        if (remainder == 0)
            return result;
        
        result += ".";
        
        unordered_map<int, int> map;    // map remainder with its index in result string
        while (remainder != 0)
        {
            // Recurring
            if (map.find(remainder) != map.end())
            {
                // Add parentheses
                result.insert(map[remainder] + 1, "(");
                result += ")";
                return result;
            }
            
            // Map remainder with its index
            map[remainder] = result.length() - 1;
            
            // Update remainder
            remainder *= 10;
            result += to_string(remainder / dividend);
            remainder %= dividend;
        }
        
        return result;
    }
};