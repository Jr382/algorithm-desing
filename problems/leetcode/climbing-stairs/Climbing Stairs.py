class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0, 1, 2]
        for i in range(3, n+1):
            mem.append(mem[i-1] + mem[i-2])
        return mem[n]
            