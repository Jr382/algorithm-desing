class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)-1
        l, r = 0, n
        while l < r:
            i = (l+r)//2
            if nums[i] > nums[r]:
                l = i+1
            elif nums[i] < nums[l]:
                r = i
            else:
                break
        
        n += 1
        return self.lower_bound(n, nums, target, n-l)

    def lower_bound(self, n: int, nums: List[int], target: int, k: int) -> int:
        l, r = 0, n
        while l < r: 
            i = (l+r)//2
            offset = (i-k)%n
            if nums[offset] == target:
                return offset
            elif nums[offset] > target:
                r = i
            else:
                l = i+1
        
        return -1