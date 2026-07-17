class Solution:
    def totalNQueens(self, n: int) -> int:
        memory = [[i] for i in range(n)]
        for row in range(1, n):
            memory = [taken+[column] for taken in memory for column in range(n) if self.is_available(taken, row, column)]
        
        return len([sol for sol in memory if len(sol) == n])
    
    def is_available(self, taken, row, column):
        for taken_row in range(len(taken)):
            if row == taken_row or column == taken[taken_row] or abs((row-taken_row)/(column-taken[taken_row])) == 1:
                return False
        
        return True