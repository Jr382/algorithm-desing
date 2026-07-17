class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size, ans, stack = len(nums), [-1]*len(nums), []
        for i in range(size):
            num = nums[i]
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            stack.append(i)
        for i in range(size):
            num = nums[i]
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            
        return ans