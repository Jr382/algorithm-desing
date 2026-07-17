class Solution:
    def trap(self, height: List[int]) -> int:
        level = 1
        total = 0
        i, j = 0, len(height) -1
        while True:
            while i < j and height[i] < level:
                i += 1
            while i < j and height[j] < level:
                j -= 1
            if height[i] < level:
                break
            low_size = min(height[i], height[j])
            total += (low_size-level+1)*(j-i+1)
            level = low_size+1

        return total - sum(height)


        

