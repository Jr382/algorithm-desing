class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        anagram = Counter(p)
        i, window = 0, Counter()
        ans = []

        for i in range(len(p)):
            if s[i] in anagram:
                window[s[i]] = window.get(s[i], 0) + 1

        k = len(p)
        for i in range(len(s) - k + 1):
            if window == anagram:
                ans.append(i)
            if i+k < len(s) and s[i+k] in anagram:
                window[s[i+k]] = window.get(s[i+k], 0) + 1
            if s[i] in anagram:
                window[s[i]] = window.get(s[i], 0) - 1
        
        return ans
            