class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j, count = 0, len(nums) - 1, 0
        while i <= j:
            if nums[j] == val:
                count += 1
                j -= 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i, j, count = i+1, j-1, count+1
            else:
                i += 1
        return len(nums)-count


        

        
            
