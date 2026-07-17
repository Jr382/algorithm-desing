class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        current, mem = 0, {0:-1}
        for i in range(len(nums)):
            current += nums[i]
            offset = current % k
            if offset not in mem:
                mem[offset] = i
            
            if i - mem.get(offset, i) > 1:
                return True

        return False