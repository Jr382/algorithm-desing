class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        from collections import deque
        form = lambda x: [nums[i] for i in x]
        ans, stack, queue = [-1]*len(nums), [], {}
        for i in range(len(nums)):
            num = nums[i]
            to_del = []
            for k in queue:
                while queue[k] and nums[queue[k][0]] < num:
                    ans[queue[k].popleft()] = num
                if not queue[k]:
                    to_del.append(k)
            for k in to_del:
                queue.pop(k)
            if stack and nums[stack[-1]] < num:
                queue[i] = deque()
            while stack and nums[stack[-1]] < num:
                queue[i].append(stack.pop())
            stack.append(i)
        
        return ans