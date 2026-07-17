class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len, start = 0, 0
        for i in range(len(s)):
            if s[i] in used and used[s[i]] >= start:
                max_len = max(max_len, i - start)
                start = used[s[i]] + 1
            used[s[i]] = i
        
        return max(max_len, len(s) - start)
