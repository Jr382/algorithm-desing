class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            current = numbers[i] + numbers[j]
            if current < target:
                i += 1
            elif current > target:
                j -= 1
            else:
                return i+1, j+1
