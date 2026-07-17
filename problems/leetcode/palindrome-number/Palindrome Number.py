class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        size, correction = len(s), len(s)%2
        return s[:size//2] == s[size//2+correction:][::-1]