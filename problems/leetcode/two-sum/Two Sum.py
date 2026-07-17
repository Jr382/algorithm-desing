class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required not in sums:
                sums[nums[i]] = i
            else:
                return [sums[required], i]
        