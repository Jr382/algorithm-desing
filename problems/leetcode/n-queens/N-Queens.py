class Solution(object):
    def solveNQueens(self, n):
        memory = [[i] for i in range(n)]
        for row in range(1, n):
            memory = [taken+[column] for taken in memory for column in range(n) if self.is_available(taken, row, column)]
        
        return [self.format(solution) for solution in memory if len(solution) == n]
        """
        :type n: int
        :rtype: List[List[str]]
        """
    
    def is_available(self, taken, row, column):
        for taken_row in range(len(taken)):
            if row == taken_row or column == taken[taken_row] or abs((row-taken_row)/(column-taken[taken_row])) == 1:
                return False
        
        return True

    def format(self, solution):
        formatted_solution = []
        for queen in solution:
            row = ""
            for i in range(len(solution)):
                row += "Q" if i == queen else "."
            formatted_solution.append(row)

        return formatted_solution