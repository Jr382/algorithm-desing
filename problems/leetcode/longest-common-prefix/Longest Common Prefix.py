class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        i, min_lenght = 0, min(len(strs[0]), len(strs[-1]))
        while i < min_lenght and strs[0][i] == strs[-1][i]:
            i += 1
        
        return strs[0][:i]
            