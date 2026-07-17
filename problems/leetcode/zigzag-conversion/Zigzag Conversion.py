class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = ["" for i in range(numRows)]
        order = [i for i in range(numRows)] + [i for i in range(numRows-2, 0, -1)]
        size = len(order)

        for i in range(len(s)):
            grid[order[i%size]] += s[i]

        return "".join(grid)
