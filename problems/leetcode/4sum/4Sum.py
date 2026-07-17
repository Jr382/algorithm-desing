class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict
        nums_set, count = [], {}
        for i in nums:
            if i not in count:
                nums_set.append(i)
                count[i] = 0
            count[i] += 1
        
        tuples = {}
        for i in range(len(nums_set)):
            for j in range(i, len(nums_set)):
                key = nums_set[i] + nums_set[j]
                if key not in tuples:
                    tuples[key] = []
                tuples[key].append((nums_set[i], nums_set[j]))
        
        feasible = []
        for i in tuples:
            if target-i in tuples:
                feasible.append((i, target-i))
        
        ans = set()
        for i1, i2 in feasible:
            for a, b in tuples[i1]:
                for c, d in tuples[i2]:
                    counter = defaultdict(int)
                    counter[a] += 1
                    counter[b] += 1
                    counter[c] += 1
                    counter[d] += 1
                    for j in counter:
                        if count[j] < counter[j]:
                            break
                    else:
                        ans.add(tuple(sorted([a,b,c,d]))) 
        return [list(i) for i in ans]