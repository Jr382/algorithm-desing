class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        mem, c = [["()"], ["()()", "(())"]], 1
        
        while len(mem) < n:
            mem.append({f"({i})" for i in mem[c]})
            c += 1
            for i in range(c//2+1):
                for par in mem[c-i-1]:
                    for par2 in mem[i]:
                        mem[c].update((par+par2, par2+par))
           
        
        return sorted(list(mem[n-1]))


            

