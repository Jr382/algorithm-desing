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