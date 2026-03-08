class Solution {
    public char nextGreatest(char[] letters, char target) 
    {
        int s = 0;
        int e = letters.length - 1;

        while (s <= e) 
        {
            int Mid = s + (e - s) / 2;

            if (letters[Mid] <= target) 
            {
                s = Mid + 1;
            }
            else 
            {
                e = Mid - 1;
            }
        }

        return letters[s % letters.length];
    }
}
