"""
Topic: Monotonic Stack
Platform: LeetCode
Time complexity: O(n log n)
Space complexity: O(1)
Explanation:
    The monotonic stack solves the first part of the problem: find the next greater number
    Now we need to find the next greater number after that greater number
    The heap allow us to keep an ordered list of the next greater number we are finding while iterating the array
    If we find a number greater than the current head of the heap then we find the second greater number for the original i position!
"""
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        from heapq import heappush, heappop
        ans, stack, heap = [-1] * len(nums), [], []
        for i in range(len(nums)):
            num = nums[i]
            while heap and heap[0][0] < num:
                ans[heappop(heap)[1]] = num
            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                heappush(heap, (nums[j], j))
            stack.append(i)

        return ans