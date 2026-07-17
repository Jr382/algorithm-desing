class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            mem.append(cost[i] + min(mem[i-1], mem[i-2]))
        
        return min(mem[-1], mem[-2])
