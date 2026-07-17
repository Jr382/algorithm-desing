class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window, i, j, max_freq = {s[0]:1}, 1, 0, 1
        while i < len(s):
            window[s[i]] = window.get(s[i], 0) + 1
            if window[s[i]] > max_freq:
                max_freq = window[s[i]]
            
            if i - j - max_freq < k:
                i += 1
                continue

            window[s[j]] -= 1
            j += 1
            i += 1

        return min(max_freq + k, len(s))