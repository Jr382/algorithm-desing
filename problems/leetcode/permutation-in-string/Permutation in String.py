class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        from collections import Counter
        s1_perm, s2_perm = Counter(s1), Counter(s2[:len(s1)])

        i = 1
        while s1_perm != s2_perm and i <= len(s2)-len(s1):
            s2_perm[s2[i-1]] -= 1
            s2_perm[s2[i+len(s1)-1]] += 1
            i += 1

        return s1_perm == s2_perm