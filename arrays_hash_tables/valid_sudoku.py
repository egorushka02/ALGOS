"""Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for row in board:
            if self.has_duplicates(row):
                return False
            
        # check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if self.has_duplicates(column):
                return False
            
        # check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [
                    board[row][col]
                    for row in range(i, i+3)
                    for col in range(j, j+3)
                ]
                if self.has_duplicates(square):
                    return False
        return True
        
        
    def has_duplicates(self, seq):
        seen = set()
        for item in seq:
            if item != '.' and item in seen:
                return True
            seen.add(item)
        return False