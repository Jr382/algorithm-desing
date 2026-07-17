class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals)
        while l < r:
            i = (l + r) // 2
            if intervals[i][0] < newInterval[0] or (intervals[i][0] == newInterval[0] and intervals[i][1] < newInterval[1]):
                l = i + 1
            else:
                r = i
        
        return self.merge(intervals[:l] + [newInterval] + intervals[l:])
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            Intervals must be sorted
        """
        ans = [intervals[0]]
        for low, up in intervals:
            if low <= ans[-1][1]:
                ans[-1][1] = max(up, ans[-1][1])
            else:
                ans.append([low, up])

        return ans
        