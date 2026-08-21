"""
Backtracking part 2
"""

"""
216. Combination Sum III
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def bt(start, acc, path_sum):
            if len(acc) == k:
                if path_sum == n:
                    result.append(acc[:])
                return

            if path_sum > n:
                return
            
            for num in range(start, 10):
                acc.append(num)
                bt(num+1, acc, path_sum+num)
                acc.pop()

        bt(1, [], 0)

        return result
    
"""
17. Letter Combinations of a Phone Number
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        if not digits:
            return result

        def bt(pos, word):
            if len(word) == len(digits):
                result.append(word)
                return
            for letter in keyboard[digits[pos]]:
                bt(pos+1, word+letter)

        bt(0, "")

        return result

"""
51. N-Queens
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []

        def bt(row, columns, diagonals, t_diagonals, board):
            if row == n:
                result.append(["".join(board[i]) for i in range(n)])
                return 
            for col in range(n):
                current_diagonal = row + col
                current_t_diagonal = row - col

                if col in columns or current_diagonal in diagonals or current_t_diagonal in t_diagonals:
                    continue
                columns.add(col)
                diagonals.add(current_diagonal)
                t_diagonals.add(current_t_diagonal)
                board[row][col] = "Q"

                bt(row+1, columns, diagonals, t_diagonals, board)

                columns.remove(col)
                diagonals.remove(current_diagonal)
                t_diagonals.remove(current_t_diagonal)
                board[row][col] = "."

        board = [["."] * n for _ in range(n)]
        bt(0, set(), set(), set(), board)

        return result
    
"""
489. Robot Room Cleaner
"""
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = set()

        def bt(x, y, direction):
            if (x, y) in visited:
                return
            visited.add((x, y))
            robot.clean()

            for i in range(len(directions)):
                new_direction = (direction + i) % len(directions)
                dx = directions[new_direction][0]
                dy = directions[new_direction][1]
                new_x = x + dx
                new_y = y + dy

                if (new_x, new_y) not in visited and robot.move():
                    bt(new_x, new_y, new_direction)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()


        bt(0, 0, 0)

        return 