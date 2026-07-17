class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)-1
        l, r = 0, n
        while l < r:
            i = (l+r)//2
            if nums[i] > nums[r]:
                l = i+1
            else:
                r = i
        return nums[l]