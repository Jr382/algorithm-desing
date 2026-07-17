"""
Topic: Sliding Window
Platform: LeetCode
Time complexity: O(n)
Space complexity: O(1)
Explanation:
    You can make the window as big as you want, but you only can reduce the window if the current sum if grater than target
    If current >= target and the size (right pointer - left pointer) is lower than the current minimum you find a new minimum :D
    PD: this can be solved in O(log n), no tried yet :/
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current = 0
        i, j = 0, 0
        min_size = len(nums)
        while j < len(nums):
            current += nums[j]
            j += 1
            while i <= j and current - nums[i] >= target:
                current -= nums[i]
                i += 1

            if current >= target:
                min_size = min(min_size, j - i)

        return 0 if current < target else min_size