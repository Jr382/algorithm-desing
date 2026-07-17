"""
Topic: Two Pointers
Platform: LeetCode
Time complexity: O(n)
Space complexity: O(1)
Explanation:
    Classical two pointer solution
    The first time slow and fast meet they are both at the same distance from the start of the cycle
    Restart slow and move both at the same time, they will meet again in the start of the cycle
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]

        return slow