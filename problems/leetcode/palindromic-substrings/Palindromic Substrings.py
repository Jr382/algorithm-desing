class Solution:
    def countSubstrings(self, s: str) -> int:
        from collections import Counter

        substrings = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                substrings.append(s[i:j+1])
        
        substrings = Counter(substrings)
        counter = 0
        for sub in substrings:
            if self.palindrome(sub):
                counter += substrings[sub]
        
        return counter
    
    def palindrome(self, s: str):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False

        return True