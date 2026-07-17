class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combinations = [i for i in letters[digits[0]]]
        for i in digits[1:]:
            new_combinations = []
            for j in letters[i]:
                for k in combinations:
                    new_combinations.append(k+j)
            combinations = new_combinations
        
        return combinations


        