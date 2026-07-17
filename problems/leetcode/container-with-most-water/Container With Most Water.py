class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        maximum = 0
        while i < j:
            if height[i] < height[j]:
                maximum = max(height[i]*(j-i), maximum)
                i += 1
            else:
                maximum = max(height[j]*(j-i), maximum)
                j -= 1
           

        return maximum