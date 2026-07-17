class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect_area, stack = 0, []
        for i in range(len(heights)):
            j = i
            while stack and heights[stack[-1][1]] > heights[i]:
                j, h = stack.pop()
                size = (i-j)*heights[h]
                if max_rect_area < size:
                    max_rect_area = size    
            stack.append((j, i))

        i += 1
        while stack:
            j, h = stack.pop()
            size = (i-j)*heights[h]
            if max_rect_area < size:
                max_rect_area = size 

        return max_rect_area

