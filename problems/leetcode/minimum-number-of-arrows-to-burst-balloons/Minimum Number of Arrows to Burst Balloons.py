class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        current = points[0]
        arrows = 1
        for interval in points:
            if current[1] >= interval[0]:
                current = (current[0], min(current[1], interval[1]))
            else:
                arrows += 1
                current = interval

        return arrows