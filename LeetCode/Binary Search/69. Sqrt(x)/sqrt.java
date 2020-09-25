class Solution {
    public int mySqrt(int x) {
        if (x == 1)
            return x;
        long left = 1;
        long right = x;
        while ( left <= right )
        {
            long mid = left + (right - left) / 2;
            if ( mid * mid <= x && (mid+1) * (mid+1) > x )
                return (int)mid;
            else if (mid * mid > x)
                right = mid - 1;
            else
            {
                left = mid + 1;
            }
        }
        return 0;
    }
}