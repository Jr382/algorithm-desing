class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans, stack = {}, []
        for num in nums2:
            while stack and stack[-1] < num:
                ans[stack.pop()] = num
            stack.append(num)
        for num in stack:
            ans[num] = -1
            
        return [ans[i] for i in nums1]