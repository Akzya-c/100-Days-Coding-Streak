import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) 
    {
        HashMap<Character, Integer> last = new HashMap<>();
        int start = 0, maxLen = 0;

        for (int i = 0; i < s.length(); i++) 
        {
            char c = s.charAt(i);
            if (last.containsKey(c) && last.get(c) >= start) 
            {
                start = last.get(c) + 1;
            }
            last.put(c, i);
            maxLen = Math.max(maxLen, i - start + 1);
        }
        return maxLen;
    }
}
