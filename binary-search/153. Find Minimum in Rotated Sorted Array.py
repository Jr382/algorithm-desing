"""
Topic: Binary Search
Platform: LeetCode
Time complexity: O(log n)
Space complexity: O(1)
Explanation:
    In a rotated sorted array with unique elements exists a position where a[i-1] > a[i] and a[i+1] > a[i]
    Modify the left bound until by comparing the middle position with the last position in the current range.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)-1
        l, r = 0, n
        while l < r:
            i = (l+r)//2
            if nums[i] > nums[r]:
                l = i+1
            else:
                r = i
        return nums[l]