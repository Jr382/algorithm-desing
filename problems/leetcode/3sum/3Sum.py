class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = set()
        pairs = {i: set() for i in nums}
        for triplet in self.twoSum(nums, 1, -nums[0]):
            triplets.add(triplet)
        for i in range(1, len(nums)): 
            if nums[i] == nums[i-1]:
                continue
            for triplet in self.twoSum(nums, i+1, -nums[i]):
                triplets.add(triplet)
        
        return [[i,j,k] for i, j, k in triplets]

    def twoSum(self, numbers: List[int], i: int, target: int) -> List[int]: 
        j = len(numbers)-1 
        triplets = set()
        while i < j: 
            current = numbers[i] + numbers[j] 
            if current < target: i += 1 
            elif current > target: j -= 1 
            else: 
                triplets.add((-target, numbers[i], numbers[j]))
                i += 1
                j -= 1
        
        return triplets