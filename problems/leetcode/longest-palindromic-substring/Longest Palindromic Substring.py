class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        palindrome = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j-i+1 > max_len and self.is_palindrome(s[i:j+1]):
                    palindrome = s[i:j+1]
                    max_len = j-i+1
        return palindrome
       
    def is_palindrome(self, s: str) -> bool:
        size, correction = len(s), len(s)%2
        return s[:size//2] == s[size//2+correction:][::-1]