class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = {}
        for i in range(len(nums)):
            if abs(i-mem.get(nums[i], i-k-1)) <= k:
                return True
            mem[nums[i]] = i
        return False
            