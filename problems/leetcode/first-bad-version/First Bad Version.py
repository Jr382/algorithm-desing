# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            i = (l+r)//2
            if isBadVersion(i):
                r = i
            else:
                l = i+1
                
        return (l+r)//2