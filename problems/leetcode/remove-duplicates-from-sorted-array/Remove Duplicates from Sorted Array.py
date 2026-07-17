class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_duplicate = 0 
        mem = set()
        for i in range(len(nums)):
            if nums[i] not in mem:
                mem.add(nums[i])
                nums[i], nums[last_duplicate] = nums[last_duplicate], nums[i]
                last_duplicate += 1

        return len(mem)
