class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["#"] * n for _ in range(n)]
        result = []

        def putQueen(row, queen):
            if row == n:
                if queen == n:
                    valid_board = []
                    for r in board:
                        valid_board.append("".join(r))
                    result.append(valid_board)
                return 
            
            seen = []
            for col in range(n):
                if board[row][col] == "#":
                    board[row][col] = "Q"
                    seen.append((row, col))

                    for i in range(n):
                        if board[row][i] == "#":
                            board[row][i] = "."
                            seen.append((row,i))
                        if board[i][col] == "#":
                            board[i][col] = "."
                            seen.append((i, col))

                    r, c = row+1, col+1
                    while 0 <= r < n and 0 <= c < n:
                        if board[r][c] == "#":
                            board[r][c] = "."
                            seen.append((r, c))
                        r += 1
                        c += 1
                        
                    r, c = row-1, col-1
                    while 0 <= r < n and 0 <= c < n:
                        if board[r][c] == "#":
                            board[r][c] = "."
                            seen.append((r, c))
                        r -= 1
                        c -= 1
                        
                    r, c = row+1, col-1
                    while 0 <= r < n and 0 <= c < n:
                        if board[r][c] == "#":
                            board[r][c] = "."
                            seen.append((r, c))
                        r += 1
                        c -= 1
                        
                    r, c = row-1, col+1
                    while 0 <= r < n and 0 <= c < n:
                        if board[r][c] == "#":
                            board[r][c] = "."
                            seen.append((r, c))
                        r -= 1
                        c += 1

                    putQueen(row+1, queen+1)

                    while seen:
                        ro, c = seen.pop()
                        board[ro][c] = "#"

        putQueen(0, 0)
        return result 