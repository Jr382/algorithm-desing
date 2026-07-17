class Solution:
    def countTriples(self, n: int) -> int:
        upper = n**2
        dic = {i**2 for i in range(5, n+1)}
        sq = [i**2 for i in range(1, n+1)]
        count = 0
        for a in range(1, n-1):
            b = a+1
            key = sq[a]+sq[b]
            while key <= upper:
                if key in dic:
                    count += 2
                b += 1
                key = sq[a]+sq[b]

        return count