class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for low, up in intervals:
            if low <= ans[-1][1]:
                ans[-1][1] = max(up, ans[-1][1])
            else:
                ans.append([low, up])

        return ans