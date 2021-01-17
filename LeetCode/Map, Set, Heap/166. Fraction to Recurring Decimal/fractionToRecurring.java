class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        StringBuilder result = new StringBuilder();
        
        // Negative result
        if ((long)numerator * denominator < 0)
            result.append("-");
        
        long divisor = Math.abs((long) numerator);
        long dividend = Math.abs((long) denominator);
        long remainder = divisor % dividend;
        
        result.append(divisor / dividend);
        
        // If no floating points
        if (remainder == 0)
            return result.toString();
        
        result.append(".");
        Map<Long, Integer> map = new HashMap<>();
        while (remainder != 0)
        {
            // Recurring
            if (map.containsKey(remainder))
            {
                // Add parenthenses
                result.insert(map.get(remainder), "(");
                result.append(")");
                break;
            }
            
            map.put(remainder, result.length());
            
            // Update remainder
            remainder *= 10;
            result.append(remainder / dividend);
            remainder %= dividend;
        }
        
        return result.toString();
    }
}