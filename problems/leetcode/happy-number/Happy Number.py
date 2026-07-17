class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.process(n)
        fast = self.process(self.process(n))
        while slow != fast:
            slow = self.process(slow)
            fast = self.process(self.process(fast))
        
        return fast == 1
        
    def process(self, n: int) -> int:
        result = 0
        while n > 0:
            d = n % 10
            n = n // 10
            result += d ** 2
            
        return result