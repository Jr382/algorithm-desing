class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, current_sum, mem = 0, 0, {0:1}
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum - k in mem:
                count += mem[current_sum - k]
            if current_sum not in mem:
                mem[current_sum] = 0
            mem[current_sum] += 1
            
        return count