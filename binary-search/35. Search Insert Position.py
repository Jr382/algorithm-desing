"""
Topic: Binary Search
Platform: LeetCode
Time complexity: O(log n)
Space complexity: O(1)
Explanation:
    My first lower bound binary search :D
    I think is cute, so I let this right as it is.
    When the target is not present in the array I will start getting the same value at certain point, breaker variable it's here to stop that haha
    Spoiler: you don't need the breaker variable
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, breaker, l, r = len(nums)//2, -1, 0, len(nums)
        while target != nums[i]:
            if breaker == i:
                break
            elif target > nums[i]:
                l = i
            else:
                r = i
            breaker = i
            i = (r+l) // 2

        return i if nums[i] >= target else i+1