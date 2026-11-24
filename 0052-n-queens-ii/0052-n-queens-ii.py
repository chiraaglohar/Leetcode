class Solution:
    def totalNQueens(self, n: int) -> int:
        position = [0] * 20
        solution_count = 0
        def is_safe(row: int, col: int) -> bool:
            for prev_row in range(row):
                if position[prev_row] == col:
                    return False
                if position[prev_row] - prev_row == col - row:
                    return False
                if position[prev_row] + prev_row == col + row:
                    return False
            return True
        def solve_nqueen(row: int):
            nonlocal solution_count
            for col in range(n):
                if is_safe(row, col):
                    position[row] = col
                    if row == n - 1:
                        solution_count += 1
                    else:
                        solve_nqueen(row + 1)
        solve_nqueen(0)
        return solution_count