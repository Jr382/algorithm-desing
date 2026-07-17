class Solution:
    def __init__(self):
        self.symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        self.substractors = {
            "I": {"V", "X"}, 
            "X": {"L", "C"}, 
            "C": {"D", "M"},
        }

    def romanToInt(self, s: str) -> int:
        total = self.symbols[s[-1]]
        for i in range(len(s) - 1):
            if s[i] in self.substractors and s[i+1] in self.substractors[s[i]]:
                total -= self.symbols[s[i]]
            else:
                total += self.symbols[s[i]]
        
        return total