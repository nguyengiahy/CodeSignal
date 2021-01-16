class Solution {
    public int minSteps(String s, String t) {
        int[] frequencies = new int[26];
        int result = 0;
        
        for (int i = 0; i < s.length(); i++)
            frequencies[s.charAt(i) - 'a']++;
        
        for (int i = 0; i < t.length(); i++)
            if (frequencies[t.charAt(i) - 'a'] > 0)
                frequencies[t.charAt(i) - 'a']--;
        
        for (int i = 0; i < 26; i++)
            result += frequencies[i];            
        
        return result;
    }
}