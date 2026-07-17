class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        counter = 0
        left, right = 0, sum(nums)
        for i in range(1, len(nums)):
            left += nums[i]
            right -= nums[i]
            if (left-right)%2 == 0:
                counter += 1
                
        return counter
        