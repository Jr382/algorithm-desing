class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        erased = -1
        current = intervals[0]
        for interval in sorted(intervals):
            if current[1] > interval[1]:
                erased += 1
                current = interval
            elif current[1] > interval[0]:
                erased += 1
            else:
                current = interval
        
        return erased
