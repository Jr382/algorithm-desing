class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        from collections import Counter, defaultdict
        nums.sort()
        tuples = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                key = nums[i]+nums[j]
                if key not in tuples:
                    tuples[key] = []
                tuples[key].append((i, j))
        
        nums.append(float("inf"))
        closest = (float("inf"), 0)
        for opt in tuples:
            i = self.binary_search(nums, target-opt)
            for i in [i, i+1]:
                diff = abs(target-nums[i]-opt)
                if diff < closest[0]:
                    for j, k in tuples[opt]:
                        if i != j and i != k:
                            closest = (diff, nums[i]+opt)
        
        return closest[1]

    def binary_search(self, lis, target):
        i, left, right, breaker = len(lis)//2, 0, len(lis), -1
        while i != breaker:
            breaker = i
            if lis[i] < target:
                left = i
            elif lis[i] == target:
                break
            else:
                right = i
            i = (left+right)//2
            
        return i
