class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        index = {}
        for i in range(len(nums)):
            if nums[i] not in index:
                index[nums[i]] = []
            index[nums[i]].append(i)
        
        total, memory = 0, {}
        for i in range(len(nums)-3, -1, -1):
            num = nums[i] // 2
            if nums[i]%2 != 0 or num not in index:
                continue

            j, k, count = len(index[num])-1, len(index[nums[i]])-1, 0
            if num in memory: 
                j, k, count = memory[num]
            
            while index[num][j] > i and j >= 0:
                while index[nums[i]][k] > index[num][j] and k >= 0:
                    k -= 1
                j -= 1
                count += len(index[nums[i]])-1-k

            memory[num] = (j, k, count)
            total += count

        return total % (10**9+7)