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
                min_size = min(min_size, j-i)
        
        return 0 if current < target else min_size