class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = self.lower_bound(nums, target)
        if lower == -1:
            return -1, -1
        
        upper = self.upper_bound(nums, target)
        return lower, upper

    def lower_bound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            i = (l+r)//2
            if nums[i] >= target: 
                r = i
            else: 
                l = i+1
        
        return l if l < len(nums) and nums[l] == target else -1
    
    def upper_bound(self, nums: List[int], target: int) -> int:
        nums.append(nums[-1]+1)
        l, r = 0, len(nums)
        while l < r:
            i = (l+r+1)//2
            if nums[i] <= target: 
                l = i
            else: 
                r = i-1

        return l if l < len(nums) and nums[l] == target else -1
