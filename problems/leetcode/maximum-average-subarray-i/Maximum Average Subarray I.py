class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n, avg = len(nums), sum(nums[:k])
        
        max_avg = avg
        for i in range(1, n-k+1):
            avg += (nums[i+k-1] - nums[i-1])
            max_avg = max(max_avg, avg)
        
        return max_avg / k
