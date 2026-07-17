"""
Topic: Two Pointers
Platform: LeetCode
Time complexity: O(log n)
Space complexity: O(1)
Explanation:
    Classical binary search solution
    The logic behind this solution is:
        Having a sorted array compare the value in the middle of the array
        If the value in the middle is greater than the target then all the values at the right can be discarded
        If the value in the middle is lower than the target then all the values at the left can be discarded
    By doing this you will be reducing the search surface in half each iteration (that's why the O(log n) time complexity)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            i = (l+r)//2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = i+1
            else:
                r = i
        return -1