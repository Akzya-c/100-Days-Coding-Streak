class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            ch = s[i]
            if ch in last and last[ch] >= start:
                start = last[ch] + 1
            last[ch] = i
            max_len = max(max_len, i - start + 1)

        return max_len
