class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        stack, ans = deque([]), [0]*(len(nums)-k+1)
        
        for i in range(k):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
        
        for i in range(k, len(nums)):
            while stack and stack[0]+k < i:
                stack.popleft()
            ans[i-k] = nums[stack[0]]
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
        
        while stack and stack[0]+k < i+1:
            stack.popleft()
        ans[-1] = nums[stack[0]]

        return ans